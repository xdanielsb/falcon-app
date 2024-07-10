import { Injectable } from '@angular/core';
import { Actions, createEffect, ofType } from '@ngrx/effects';
import * as GraphActions from './graph.actions';
import { catchError, map, mergeMap, switchMap, tap } from 'rxjs/operators';
import { GraphService } from '../services/graph.service';
import { of } from 'rxjs';
import { Graph } from '../models/graph';
import { Store } from '@ngrx/store';
import { ShortestPath } from '../models/shortest-path';
import { GraphInfo } from '../models/graph-info';
@Injectable()
export class GraphEffects {
  getGraph$ = createEffect(() =>
    this.actions$.pipe(
      ofType(GraphActions.getGraph),
      switchMap(() => {
        return this.graphService.getGraph().pipe(
          map((graph: Graph) =>
            GraphActions.getGraphSuccess({
              nodes: graph.nodes,
              edges: graph.edges,
            }),
          ),
          catchError((error) =>
            of(GraphActions.getGraphFailure({ error: error.message })),
          ),
        );
      }),
      tap(() => {
        this.store$.dispatch(GraphActions.getGraphInfo());
      }),
    ),
  );

  computeOdds$ = createEffect(() =>
    this.actions$.pipe(
      ofType(GraphActions.getOddsPath),
      switchMap((action) => {
        return this.graphService
          .computeOdds({
            sourceId: action.sourceId,
            targetId: action.targetId,
            autonomy: action.autonomy,
          })
          .pipe(
            map((shortestPath: ShortestPath) =>
              GraphActions.getOddsPathSuccess({
                shortestPath: shortestPath,
              }),
            ),
            catchError((error) =>
              of(GraphActions.getOddsFailure({ error: error.message })),
            ),
          );
      }),
    ),
  );

  getGraphInfo$ = createEffect(() =>
    this.actions$.pipe(
      ofType(GraphActions.getGraphInfo),
      switchMap(() => {
        return this.graphService.getGraphInfo().pipe(
          map((graphInfo: GraphInfo) =>
            GraphActions.getGraphInfoSuccess({
              graphInfo: graphInfo,
            }),
          ),
          catchError((error) =>
            of(GraphActions.getGraphInfoFailure({ error: error.message })),
          ),
        );
      }),
    ),
  );

  constructor(
    private actions$: Actions,
    private store$: Store,
    private graphService: GraphService,
  ) {}
}
