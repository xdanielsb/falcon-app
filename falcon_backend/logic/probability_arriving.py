from falcon_backend.logger import get_logger
from graph_app.types.empire import BountyHunterWithPlanetId
from graph_app.types.graph_desc import FindPathReturnType


def compute_probability_arrival(
    target_id: int,
    path_info: FindPathReturnType,
    countdown: int,
    bounty_hunters: list[BountyHunterWithPlanetId],
    stops: list[int],
) -> float:
    """
    Compute the probability of the falcon given they arrive to the destination
    """

    (distance_dict, path) = path_info

    if path is None or distance_dict is None:
        # sanity check
        get_logger().info("Path or distance dict is None probability is zero")
        return 0.0

    if distance_dict[target_id] > countdown:
        get_logger().info("Distance is greater than countdown probability is zero")
        return 0.0

    ans = 1.0
    times = 0  # ntimes has crossed with a bounty hunter
    node_ids_with_bounty_hunters = [hunter.node_id for hunter in bounty_hunters]
    for node_id, value in distance_dict.items():
        if node_id in node_ids_with_bounty_hunters:
            if times == 0:
                ans -= 1 / 10
            else:
                ans -= (9**times) / (10 ** (times + 1))
            times += 1

    #  iterate on stops in case of repeated stops
    for stop in stops:
        if stop in distance_dict.keys():
            if times == 0:
                ans -= 1 / 10
            else:
                ans -= (9**times) / (10 ** (times + 1))
            times += 1
    return ans
