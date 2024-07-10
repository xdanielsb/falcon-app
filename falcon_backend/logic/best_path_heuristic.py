import random
from typing import TYPE_CHECKING

from falcon_backend.logger import get_logger
from logic.find_path import get_find_path_with_autonomy

if TYPE_CHECKING:
    from graph_app.types.graph_desc import FindPathReturnType, AdjListType


def modify_one_edge_to_infinity(adj_lists: "AdjListType", best_current_path: list[int]):
    len_path = len(best_current_path)

    if len_path < 2:
        return adj_lists

    modified_adj_lists = adj_lists.copy()
    random_index = random.randint(0, len_path - 2)
    count = 0
    for node, weight in modified_adj_lists[best_current_path[random_index]]:
        if node == best_current_path[random_index + 1]:
            modified_adj_lists[best_current_path[random_index]][count] = (
                node,
                float("inf"),
            )
            get_logger().info(
                f"Modified edge to infinity {best_current_path[random_index]} -> {node} = inf"
            )
            break
        else:
            count += 1

    return modified_adj_lists


def find_best_path_heuristic(
    source: int,
    target: int,
    adj_lists: "AdjListType",
    initial_autonomy: int,
    iterations=5,
) -> "FindPathReturnType":
    """
    Since from source node to target node can be infinite path, I implemented a heuristic algorithm, the idea
    is to find the best path using djikstra algorithm, but in each iteration, I will modify one edge to infinity
    of that best path so that the algorithm will find another path, and I will keep the best path found until
    the end of the iterations
    """
    best_distance = float("inf")
    best_path = None
    best_stops = []
    best_total_distance_dict = {}

    for i in range(iterations):
        modified_adj_lists = (
            modify_one_edge_to_infinity(adj_lists, best_path)
            if best_path is not None
            else adj_lists.copy()
        )
        distance_dict, path, stops = get_find_path_with_autonomy(
            source, target, modified_adj_lists, initial_autonomy
        )
        if path is not None:
            total_distance = distance_dict[target]
            if total_distance < best_distance:
                best_distance = total_distance
                best_path = path
                best_stops = stops
                best_total_distance_dict = distance_dict
        get_logger().info(
            f"Best path found so far: {best_path}, with distance: {best_distance}, iteration {i} / {iterations}"
        )

    return best_total_distance_dict, best_path, best_stops
