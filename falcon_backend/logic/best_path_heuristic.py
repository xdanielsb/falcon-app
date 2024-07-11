import random
from typing import TYPE_CHECKING

from graph_app.types.empire import BountyHunterWithPlanetId
from logic.find_path import get_find_path_with_autonomy
from logic.probability_arriving import compute_probability_arrival

if TYPE_CHECKING:
    from graph_app.types.graph_desc import FindPathReturnType, AdjListType


def get_random_node_to_disable(best_current_path: list[int]):
    len_path = len(best_current_path)

    if len_path <= 2:
        return None

    random_index = random.randint(1, len_path - 2)
    return best_current_path[random_index]


def find_best_path_heuristic(
    source: int,
    target: int,
    adj_lists: "AdjListType",
    initial_autonomy: int,
    countdown: int,
    bounty_hunters: list[BountyHunterWithPlanetId],
    iterations=5,
) -> "FindPathReturnType":
    """
    Finds the best path (distance, stops, probability of arrival) considering limited
    autonomy, bounty hunters, and refueling needs.

    This function implements a heuristic approach to handle potentially infinite paths.
    meaning that will not assure to arrive to a global maximum, but it will try to find a good path ^^
    It iteratively utilizes a variation of Dijkstra's algorithm. In each iteration,
    a random non-source and non-target node from the current best path is disabled,
    forcing the algorithm to explore alternative routes. The function tracks the
    best path found so far based on probability.
    """
    best_path = None
    best_stops = []
    best_total_distance_dict = {}
    best_probability = 0.0

    for i in range(iterations):
        if best_path is None:
            disabled_node = None
        else:
            disabled_node = get_random_node_to_disable(best_path)

        distance_dict, path, node_ids_refuel = get_find_path_with_autonomy(
            source, target, adj_lists, initial_autonomy, [disabled_node]
        )

        probability_arriving = compute_probability_arrival(
            target,
            (distance_dict, path),
            countdown,
            bounty_hunters,
            node_ids_refuel,
        )
        if probability_arriving > best_probability:
            best_probability = probability_arriving
            best_path = path
            best_stops = node_ids_refuel
            best_total_distance_dict = distance_dict

    return best_total_distance_dict, best_path, best_stops, best_probability
