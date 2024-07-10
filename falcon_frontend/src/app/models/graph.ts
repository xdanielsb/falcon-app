import { EdgeResponse, parseEdgeResponse } from './edge';
import { NodeResponse, parseResponseNode } from './node';

export interface GraphMetadataForm {
  sourceId: string | number | null;
  targetId: string | number | null;
  autonomy: string | number | null;
}

export interface GraphResponse {
  nodes: NodeResponse[];
  edges: EdgeResponse[];
}

export const parseGraph = ({ nodes, edges }: GraphResponse) => {
  return {
    nodes: nodes.map(parseResponseNode),
    edges: edges.map(parseEdgeResponse),
  };
};
