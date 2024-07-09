from queue import PriorityQueue
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from falcon_backend.tests.test_shortest_path import AdjListType


def get_shortest_path_with_autonomy(
    source: int,
    target: int,
    adj_lists: "AdjListType",
    initial_autonomy: int | None = None,
) -> tuple[dict[int, int] | None, list[int] | None]:
    """
    Compute the shortest path from departure to destiny
    it receives a dictionary with the adjacency lists of the graph
    and the autonomy that reflects that the vehicle can travel
    without refueling autonomy units of distance without refueling
    """
    if source not in adj_lists or target not in adj_lists:
        raise ValueError("Source or destination does not exists in edges")

    if initial_autonomy < 0:
        raise ValueError("Initial autonomy must be greater or equal to zero")

    if initial_autonomy is None:
        initial_autonomy = float("inf")
    pq = PriorityQueue()
    # [distance from departure, node, autonomy]
    pq.put((0, source, initial_autonomy))
    # nodes already visited
    visited = set()
    # distance from departure to each node
    distance_dict = {source: 0}
    # parent of each node, helps to rebuild the path
    parent = {}
    # whether the paint is reach
    path_found = False
    # number of times it had to refuel
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
                if (
                    connection not in distance_dict
                    or distance_dict[connection] > d + weight
                ):
                    distance_dict[connection] = d + weight
                    parent[connection] = node
                    pq.put((distance_dict[connection], connection, autonomy - weight))

    if not path_found:
        return None, None

    # rebuild the path
    path = [target]
    curr = target
    while curr != source:
        curr = parent[curr]
        path.append(curr)

    # only return the dis of nodes in path
    distance_dict = {key: value for key, value in distance_dict.items() if key in path}
    return distance_dict, path
