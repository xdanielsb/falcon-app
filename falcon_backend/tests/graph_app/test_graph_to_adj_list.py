from django.test import TestCase

from graph_app.models import Node, Edge
from graph_app.utils.graph import graph_to_adj_list


class TestGraphToAdjList(TestCase):
    def setUp(self):
        # Create some nodes for testing
        Node.objects.all().delete()
        Edge.objects.all().delete()
        self.node1 = Node.objects.create(name="node1")
        self.node2 = Node.objects.create(name="node2")
        self.node3 = Node.objects.create(name="node3")

    def test_simple_graph_to_adj_list(self):
        Edge.objects.create(source=self.node1, target=self.node2, weight=3)
        Edge.objects.create(source=self.node2, target=self.node3, weight=4)
        Edge.objects.create(source=self.node3, target=self.node1, weight=2)

        edges = Edge.objects.all()
        adj_lists = graph_to_adj_list(edges)
        expected = {1: [(2, 3), (3, 2)], 2: [(1, 3), (3, 4)], 3: [(2, 4), (1, 2)]}

        self.assertEqual(adj_lists, expected)

    def test_transform_when_no_edges(self):
        edges = []
        adj_lists = graph_to_adj_list(edges)
        self.assertEqual(adj_lists, {})
