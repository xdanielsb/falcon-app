from typing import TYPE_CHECKING

from graph_app.models import Edge

if TYPE_CHECKING:
    from tests.logic.test_shortest_path import AdjListType


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
