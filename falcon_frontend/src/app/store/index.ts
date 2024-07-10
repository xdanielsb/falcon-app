import { Node, Edge } from '@swimlane/ngx-graph';
import { ShortestPath } from '../models/shortest-path';

export interface GlobalState {
  graphState: GraphState;
}

export interface GraphState {
  isLoading: boolean;
  nodes: Node[];
  edges: Edge[];
  error: string | null;
  shortestPath: ShortestPath | null;
}

export const initialState: GraphState = {
  isLoading: false,
  nodes: [],
  edges: [],
  error: null,
  shortestPath: null,
};
