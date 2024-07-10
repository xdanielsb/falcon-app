import { EdgeResponse, parseEdgeResponse } from './edge';
import { NodeResponse, parseResponseNode } from './node';
import { Edge, Node } from '@swimlane/ngx-graph';

export interface GraphMetadataForm {
  sourceId: string | number | null;
  targetId: string | number | null;
  autonomy: string | number | null;
}

export interface GraphResponse {
  nodes: NodeResponse[];
  edges: EdgeResponse[];
}

export interface Graph {
  nodes: Node[];
  edges: Edge[];
}

export const parseGraph = ({ nodes, edges }: GraphResponse): Graph => {
  return {
    nodes: nodes.map(parseResponseNode),
    edges: edges.map(parseEdgeResponse),
  };
};
