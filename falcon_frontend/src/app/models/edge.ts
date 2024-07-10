export interface EdgeResponse {
  source: number;
  target: number;
  weight: number;
}

export const parseEdgeResponse = (response: EdgeResponse) => {
  return {
    source: response.source.toString(),
    target: response.target.toString(),
    label: response.weight.toString(),
  };
};
