from queue import PriorityQueue


def get_shortest_path_with_autonomy(
    departure: int,
    destiny: int,
    adj_lists: dict[int, list[int]],
    initial_autonomy: int | None = None,
):
    """
    Compute the shortest path from departure to destiny
    it receives a dictionary with the adjacency lists of the graph
    and the autonomy that reflects that the vehicle can travel
    without refueling autonomy units of distance without refueling
    """
    pq = PriorityQueue()
    # [distance from departure, node, autonomy]
    pq.put((0, departure, initial_autonomy))
    # nodes already visited
    visited = set()
    # distance from departure to each node
    dis = {departure: 0}
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

        if node == destiny:
            path_found = True
            break

        if node in adj_lists:
            for neighbor, weight in adj_lists[node]:
                if neighbor not in dis or dis[neighbor] > d + weight:
                    dis[neighbor] = d + weight
                    parent[neighbor] = node
                    pq.put((dis[neighbor], neighbor, autonomy - weight))

    if not path_found:
        return {}, [], 0

    # rebuild the path
    path = [destiny]
    curr = destiny
    while curr != departure:
        curr = parent[curr]
        path.append(curr)

    # only return the dis of nodes in path
    dis = {key: value for key, value in dis.items() if key in path}
    return dis, path
