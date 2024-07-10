import { createReducer, on } from '@ngrx/store';
import * as GraphActions from './graph.actions';
import { GraphState, initialState } from './index';

export const graphReducers = createReducer(
  initialState,
  // get graph
  on(GraphActions.getGraph, (state: GraphState) => ({
    ...state,
    isLoading: true,
  })),
  on(GraphActions.getGraphSuccess, (state: GraphState, action) => ({
    ...state,
    isLoading: false,
    nodes: action.nodes,
    edges: action.edges,
  })),
  on(GraphActions.getGraphFailure, (state: GraphState, action) => ({
    ...state,
    isLoading: false,
    error: action.error,
  })),
  // get odds info
  on(GraphActions.getOddsPath, (state: GraphState) => ({
    ...state,
    isLoading: true,
  })),
  on(GraphActions.getOddsPathSuccess, (state: GraphState, action) => ({
    ...state,
    isLoading: false,
    graphPath: action.graphPath,
  })),
  on(GraphActions.getOddsFailure, (state: GraphState, action) => ({
    ...state,
    isLoading: false,
    error: action.error,
  })),
  // get graph info
  on(GraphActions.getGraphInfo, (state: GraphState) => ({
    ...state,
    isLoading: true,
  })),
  on(GraphActions.getGraphInfoSuccess, (state: GraphState, action) => ({
    ...state,
    isLoading: false,
    graphInfo: action.graphInfo,
  })),
  on(GraphActions.getGraphInfoFailure, (state: GraphState, action) => ({
    ...state,
    isLoading: false,
    error: action.error,
  })),
);
