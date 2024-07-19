import random
from typing import TYPE_CHECKING

from graph_app.models import Edge, Node, GraphMetadata

if TYPE_CHECKING:
    from tests.logic.test_find_path import AdjListType


def graph_to_adj_list(edges: list[Edge]) -> "AdjListType":
    """
    Convert a list of edges to an adjacency list
    """
    adj_lists = {}
    for edge in edges:
        if edge.source.pk not in adj_lists:
            adj_lists[edge.source.pk] = []
        if edge.target.pk not in adj_lists:
            adj_lists[edge.target.pk] = []
        adj_lists[edge.source.pk].append((edge.target.pk, edge.weight))
        # can go in both directions
        adj_lists[edge.target.pk].append((edge.source.pk, edge.weight))
    return adj_lists


def create_random_graph() -> None:
    # Clear existing data
    Node.objects.all().delete()
    Edge.objects.all().delete()
    GraphMetadata.objects.all().delete()

    num_nodes = random.randint(5, 10)
    nodes = []
    for i in range(num_nodes):
        node = Node.objects.create(name=f"Planet {i}")
        nodes.append(node)
    for i in range(0, num_nodes):
        for j in range(i + 1, i + 1 + random.randint(1, 3)):
            if j < num_nodes:
                Edge.objects.create(
                    source=nodes[i],
                    target=nodes[j],
                    weight=random.randint(1, 10),
                )
    GraphMetadata.objects.create(
        source=nodes[0], target=nodes[num_nodes - 1], autonomy=10
    )
