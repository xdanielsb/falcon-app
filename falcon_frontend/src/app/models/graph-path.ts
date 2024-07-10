export interface DistanceMap {
  [nodeKey: string]: number;
}

export interface GraphPath {
  distances: DistanceMap;
  path: number[];
  probability: number;
}
