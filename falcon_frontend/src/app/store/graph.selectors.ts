import { GlobalState, GraphState } from './index';
import { createSelector } from '@ngrx/store';

export const selectFeature = (state: GlobalState) => state.graphState;
export const isLoadingSelector = createSelector(
  selectFeature,
  (state) => state.isLoading,
);

export const graphSelector = createSelector(selectFeature, (state) => {
  return { nodes: state.nodes, edges: state.edges };
});

export const shortestPathSelector = createSelector(selectFeature, (state) => {
  return state.shortestPath;
});

export const graphInfoSelector = createSelector(selectFeature, (state) => {
  return state.graphInfo;
});
