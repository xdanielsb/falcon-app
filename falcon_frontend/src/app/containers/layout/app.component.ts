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

  constructor(
    private graphService: GraphService,
    private store$: Store<GlobalState>,
  ) {
    this.store$.dispatch(GraphActions.getGraph());
    this.store$
      .pipe(select(GraphSelectors.isLoadingSelector))
      .subscribe((loading) => (this.loading = loading));
    this.store$
      .pipe(
        select(GraphSelectors.graphSelector),
        tap((graph: Graph) => {
          this.graph = graph;
        }),
      )
      .subscribe();
    this.store$
      .pipe(
        select(GraphSelectors.findPathSelector),
        tap((res: GraphPath | null) => {
          if (this.graph && res) {
            this.odds = res.probability;
            const nodes: Node[] = (this.graph?.nodes || []).map((node) => {
              return {
                ...node,
                data: {
                  ...node.data,
                  selected: res.path.includes(Number(node.id)),
                },
              };
            });
            this.graph = { ...this.graph, nodes };
          }
        }),
      )
      .subscribe();

    this.store$
      .pipe(
        select(GraphSelectors.graphInfoSelector),
        tap((graphInfo: GraphInfo | null) => {
          this.graphInfo = graphInfo;
        }),
      )
      .subscribe();
  }

  computeOdds(input: GraphMetadataForm) {
    const params = {
      sourceId: Number(input.sourceId),
      targetId: Number(input.targetId),
      autonomy: Number(input.autonomy),
    };
    this.store$.dispatch(GraphActions.getOddsPath(params));
  }
}
