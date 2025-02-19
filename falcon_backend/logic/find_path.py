from queue import PriorityQueue
from typing import TYPE_CHECKING
from falcon_backend.logger import get_logger


if TYPE_CHECKING:
    from graph_app.types.graph_desc import FindPathReturnType, AdjListType


def get_find_path_with_autonomy(
    source: int,
    target: int,
    adj_lists: "AdjListType",
    initial_autonomy: int | None = None,
    disabled_nodes: list[int] | None = None,
) -> "FindPathReturnType":
    """
    Find a path from departure to destiny, djiikstra algorithm with a twist :)

    it receives a dictionary with the adjacency lists of the graph
    and the autonomy that reflects that the vehicle can travel
    without refueling autonomy units of distance without refueling

    it returns a tuple with the distance from the departure to each node
    the path from the source to the target node and the nodes where stops to refuel

    """
    if source not in adj_lists or target not in adj_lists:
        get_logger().error("Source or destination does not exists in edges")
        raise ValueError("Source or destination does not exists in edges")

    # first check for none to avoid comparing a none with a number
    if initial_autonomy is None:
        get_logger().info("Initial autonomy is not provided, setting it to infinity")
        initial_autonomy = float("inf")

    if initial_autonomy < 0:
        get_logger().error("Initial autonomy must be greater or equal to zero")
        raise ValueError("Initial autonomy must be greater or equal to zero")

    pq = PriorityQueue()
    # [distance from departure, node, autonomy]
    pq.put((0, source, initial_autonomy))
    # nodes already visited
    visited = set()
    # distance from departure to each node
    distance_dict = {source: 0}
    # parent of each node, helps to rebuild the path
    parent = {}
    # store the nodes ids where the vehicle stops to refuel
    node_ids_of_refuel = []
    # whether the paint is reach
    path_found = False
    # number of times it had to refuel

    if disabled_nodes is not None:
        for disabled_node in disabled_nodes:
            visited.add(disabled_node)

    while not pq.empty():
        d, node, autonomy = pq.get()

        if node in visited:
            continue
        visited.add(node)

        if node == target:
            path_found = True
            break

        if node in adj_lists:
            for connection, weight in adj_lists[node]:
                if disabled_nodes is not None and connection in disabled_nodes:
                    continue
                if autonomy - weight >= 0:
                    if (
                        connection not in distance_dict
                        or distance_dict[connection] > d + weight
                    ):
                        distance_dict[connection] = d + weight
                        parent[connection] = node
                        pq.put(
                            (distance_dict[connection], connection, autonomy - weight)
                        )
                elif initial_autonomy >= weight:
                    # if autonomy is not enough, refuel and go to neighbor
                    # +1 because refueling takes 1 time unit
                    if (
                        connection not in distance_dict
                        or distance_dict[connection] > d + weight + 1
                    ):
                        distance_dict[connection] = d + weight + 1
                        parent[connection] = node
                        pq.put(
                            (
                                distance_dict[connection],
                                connection,
                                initial_autonomy - weight,
                            )
                        )
                        # the stop is in the current node not in the connection
                        node_ids_of_refuel.append(node)

    if not path_found:
        return None, None, []

    # rebuild the path
    path = [target]
    curr = target
    while curr != source:
        curr = parent[curr]
        path.append(curr)

    # only return the dis of nodes in path
    distance_dict = {key: value for key, value in distance_dict.items() if key in path}
    node_ids_of_refuel = [stop for stop in node_ids_of_refuel if stop in path]
    return distance_dict, path, node_ids_of_refuel
