import { Hunter } from './hunter';

export interface GraphInfo {
  numberOfNodes: number;
  numberOfEdges: number;
  countDown: number;
  hunters: Hunter[];
  sourceId: number;
  targetId: number;
  autonomy: number;
}
