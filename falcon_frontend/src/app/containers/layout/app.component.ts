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
import { ShortestPath } from '../../models/shortest-path';

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
  ],
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrl: './app.component.scss',
})
export class AppComponent {
  loading = false;
  graph: Graph | null = null;
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
        select(GraphSelectors.shortestPathSelector),
        tap((res: ShortestPath | null) => {
          if (this.graph && res) {
            this.odds = res.probability;
            console.log(this.odds);
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
