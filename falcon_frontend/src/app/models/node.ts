import { Node } from '@swimlane/ngx-graph';

export interface NodeResponse {
  pk: number;
  name: string;
}

export const parseResponseNode = (response: NodeResponse): Node => {
  return {
    id: response.pk.toString(),
    label: response.name,
  };
};
