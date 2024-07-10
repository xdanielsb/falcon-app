import { createAction, props } from '@ngrx/store';
import { Node, Edge } from '@swimlane/ngx-graph';
import { GraphPath } from '../models/graph-path';
import { GraphInfo } from '../models/graph-info';
// graph
export const getGraph = createAction('[Graph] Get graph');
export const getGraphSuccess = createAction(
  '[Graph] Get graph success',
  props<{ nodes: Node[]; edges: Edge[] }>(),
);
export const getGraphFailure = createAction(
  '[Graph] Get graph failure',
  props<{ error: string }>(),
);

// shortest path
export const getOddsPath = createAction(
  '[Graph] Get odds info',
  props<{ sourceId: number; targetId: number; autonomy: number }>(),
);
export const getOddsPathSuccess = createAction(
  '[Graph] Get odds success',
  props<{ graphPath: GraphPath }>(),
);
export const getOddsFailure = createAction(
  '[Graph] Get odds failure',
  props<{ error: string }>(),
);

// graph info
export const getGraphInfo = createAction('[Graph] Get graph info');
export const getGraphInfoSuccess = createAction(
  '[Graph] Get graph info success',
  props<{ graphInfo: GraphInfo }>(),
);
export const getGraphInfoFailure = createAction(
  '[Graph] Get graph info failure',
  props<{ error: string }>(),
);
