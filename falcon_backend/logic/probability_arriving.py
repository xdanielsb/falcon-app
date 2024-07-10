from falcon_backend.logger import get_logger
from graph_app.types.empire import BountyHunterWithPlanetId
from graph_app.types.graph_desc import FindPathReturnType


def compute_probability_arrival(
    target_id: int,
    path_info: FindPathReturnType,
    countdown: int,
    bounty_hunters: list[BountyHunterWithPlanetId],
    node_ids_of_refuel: list[int],
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

    free_days = countdown - distance_dict[target_id]

    ans = 1.0
    times = 0  # ntimes has crossed with a bounty hunter
    node_ids_with_bounty_hunters = [hunter.node_id for hunter in bounty_hunters]
    days_buy_by_nodes_id = {hunter.day: hunter.node_id for hunter in bounty_hunters}
    nodes_without_bounty_hunters = []
    distance_dict = [
        [a, b] for (a, b) in sorted(distance_dict.items(), key=lambda item: item[1])
    ]
    for index, (node_id, passed_days) in enumerate(distance_dict):
        if node_id not in node_ids_with_bounty_hunters:
            nodes_without_bounty_hunters.append([node_id, index])
            continue
        count = node_ids_of_refuel.count(node_id)
        for c in range(count + 1):
            if node_id == days_buy_by_nodes_id.get(passed_days + c):
                if free_days > 0 and len(nodes_without_bounty_hunters) > 0:
                    last_node, index = nodes_without_bounty_hunters[
                        len(nodes_without_bounty_hunters) - 1
                    ]
                    distance_dict = [
                        [a, b + 1]
                        for i, (a, b) in enumerate(distance_dict)
                        if i >= index
                    ]
                    free_days -= 1
                    # incremente the sum of all nodes after node_id
                    continue
                # if the falcon arrives to the node with a bounty hunter and the day is the same
                if times == 0:
                    ans -= 1 / 10
                else:
                    ans -= (9**times) / (10 ** (times + 1))
                times += 1
    return ans
