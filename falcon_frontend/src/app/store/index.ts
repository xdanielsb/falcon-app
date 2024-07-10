import { Node, Edge } from '@swimlane/ngx-graph';
import { GraphPath } from '../models/graph-path';
import { GraphInfo } from '../models/graph-info';

export interface GlobalState {
  graphState: GraphState;
}

export interface GraphState {
  isLoading: boolean;
  nodes: Node[];
  edges: Edge[];
  error: string | null;
  graphPath: GraphPath | null;
  graphInfo: GraphInfo | null;
}

export const initialState: GraphState = {
  isLoading: false,
  nodes: [],
  edges: [],
  error: null,
  graphPath: null,
  graphInfo: null,
};
