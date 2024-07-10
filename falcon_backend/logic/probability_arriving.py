from graph_app.models import Empire
from graph_app.types.graph_desc import ShortestPathReturnType


def compute_probability_arrival(
    target_id: int, path_info: ShortestPathReturnType, empire: Empire
) -> float:
    """
    Compute the probability of the falcon given they arrive to the destination
    """

    (distance_dict, path) = path_info

    if path is None or distance_dict is None:
        return 0

    if distance_dict[target_id] >= empire.countdown:
        return 0

    # here do the logic to compute the probability

    return 1.0
