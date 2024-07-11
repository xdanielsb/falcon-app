from typing import Tuple, Dict, List

# describe a single adjacency list
AdjListType = Dict[int, List[Tuple[int, int]]]

# type describe a graph as adjacency lists
GraphDescType = Tuple[Dict[str, int], AdjListType]

# type describe the return of the find path function
# {distances, path, probability}
FindPathReturnType = Tuple[Dict[int, int] | None, List[int] | None, float]
