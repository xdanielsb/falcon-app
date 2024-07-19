import { ChangeDetectorRef, Component } from '@angular/core';
import { RouterModule } from '@angular/router';
import {
  MatDrawer,
  MatDrawerContainer,
  MatDrawerContent,
} from '@angular/material/sidenav';
import { GraphFormComponent } from '../../components/graph-form/graph-form.component';
import { GraphSettingsComponent } from '../../components/graph-settings/graph-settings.component';
import { GraphService } from '../../services/graph.service';
import { Graph, GraphMetadataForm } from '../../models/graph';
import { TranslateModule } from '@ngx-translate/core';
import { Observable } from 'rxjs';
import { GraphPreviewComponent } from '../../components/graph-preview/graph-preview.component';
import { select, Store } from '@ngrx/store';
import { GlobalState } from '../../store';

import { Edge, Node } from '@swimlane/ngx-graph';

import * as GraphActions from '../../store/graph.actions';
import * as GraphSelectors from '../../store/graph.selectors';
import { tap } from 'rxjs/operators';
import { GraphPath } from '../../models/graph-path';
import { GraphInfoComponent } from '../../components/graph-info/graph-info.component';
import { GraphInfo } from '../../models/graph-info';
import { MatIcon } from '@angular/material/icon';
import { MatMiniFabButton } from '@angular/material/button';
import { GraphOptionsComponent } from '../../components/graph-options/graph-options.component';

@Component({
  standalone: true,
  imports: [
    RouterModule,
    MatDrawerContainer,
    MatDrawer,
    MatDrawerContent,
    GraphFormComponent,
    GraphSettingsComponent,
    TranslateModule,
    GraphPreviewComponent,
    GraphInfoComponent,
    MatIcon,
    MatMiniFabButton,
    GraphOptionsComponent,
  ],
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrl: './app.component.scss',
})
export class AppComponent {
  loading = false;
  graph: Graph | null = null;
  graphInfo: GraphInfo | null = null;
  odds: number | null = null;
  minDistance: number | null = null;

  constructor(
    private graphService: GraphService,
    private store$: Store<GlobalState>,
  ) {
    // dispatch the action to get the graph
    this.store$.dispatch(GraphActions.getGraph());
    // subscribe to the loading state
    this.store$
      .pipe(select(GraphSelectors.isLoadingSelector))
      .subscribe((loading) => (this.loading = loading));
    // subscribe to the graph state
    this.store$
      .pipe(
        select(GraphSelectors.graphSelector),
        tap((graph: Graph) => {
          this.graph = graph;
        }),
      )
      .subscribe();
    // subscribe to the odds path state, the odds as well return the path
    // when is returned the nodes in the path are marked as selected
    // this help to change its color to white
    this.store$
      .pipe(
        select(GraphSelectors.findPathSelector),
        tap((res: GraphPath | null) => {
          if (this.graph && res) {
            this.odds = res.probability;
            this.minDistance = Math.max(...Object.values(res.distances));
            const nodes: Node[] = (this.graph?.nodes || []).map((node) => {
              return {
                ...node,
                data: {
                  ...node.data,
                  selected: res.path
                    ? res.path.includes(Number(node.id))
                    : false,
                },
              };
            });
            this.graph = { ...this.graph, nodes };
          }
        }),
      )
      .subscribe();
    // this is the initial info of the graph loaded from the .json file
    // stored in the db
    this.store$
      .pipe(
        select(GraphSelectors.graphInfoSelector),
        tap((graphInfo: GraphInfo | null) => {
          this.graphInfo = graphInfo;
        }),
      )
      .subscribe();
  }

  /** dispatch the action to get the odds and path */
  computeOdds(input: GraphMetadataForm) {
    this.store$.dispatch(
      GraphActions.getOddsPath({
        sourceId: Number(input.sourceId),
        targetId: Number(input.targetId),
        autonomy: input.autonomy,
        countdown: input.countdown,
      }),
    );
  }

  /** dispatch the action to get the graph */
  createRandomGraph() {
    this.store$.dispatch(GraphActions.createGraph({ random: true }));
  }
}
