export interface NodeResponse {
  pk: number;
  name: string;
}

export const parseResponseNode = (response: NodeResponse) => {
  return {
    // id is better understood
    id: response.pk.toString(),
    label: response.name,
  };
};
