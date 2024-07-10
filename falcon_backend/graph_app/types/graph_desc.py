from typing import Tuple, Dict, List

AdjListType = Dict[int, List[Tuple[int, int]]]

GraphDescType = Tuple[Dict[str, int], AdjListType]

FindPathReturnType = Tuple[Dict[int, int] | None, List[int] | None, float]
