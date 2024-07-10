export interface DistanceMap {
  [nodeKey: string]: number;
}

export interface ShortestPath {
  distances: DistanceMap;
  path: number[];
  probability: number;
}
