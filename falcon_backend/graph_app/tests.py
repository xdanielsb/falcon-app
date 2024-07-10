from django.test import override_settings, TestCase
from django.urls import path, reverse
from rest_framework import status
from rest_framework.test import APITestCase, URLPatternsTestCase

from graph_app.models import Edge, Node
from graph_app.utils.graph import graph_to_adj_list
from graph_app.views import graph_view, ShortestPathView


class APIGraphTests(APITestCase, URLPatternsTestCase):
    urlpatterns = [
        path("graph/", graph_view, name="graph"),
    ]

    @override_settings(DEBUG=True)
    def test_get_graph_without_data(self):
        response = self.client.get(reverse("graph"), format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {"nodes": [], "edges": []})

    @override_settings(DEBUG=True)
    def test_get_graph_with_data(self):
        # initialize the graph
        self.node1 = Node.objects.create(name="node1")
        self.node2 = Node.objects.create(name="node2")
        self.edge1 = Edge.objects.create(source=self.node1, target=self.node2, weight=1)

        # retrieve the graph
        response = self.client.get(reverse("graph"), format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        nodes = (node["pk"] for node in response.data["nodes"])
        edges = (edge["pk"] for edge in response.data["edges"])
        self.assertEqual(set(nodes), {self.node1.pk, self.node2.pk})
        self.assertEqual(set(edges), {self.edge1.pk})

        # Clean up
        self.node1.delete()
        self.node2.delete()
        self.edge1.delete()


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
        expected = {1: [(2, 3), (1, 3)], 2: [(3, 4), (2, 4)], 3: [(1, 2), (3, 2)]}
        self.assertEqual(adj_lists, expected)

    def test_transform_when_no_edges(self):
        edges = []
        adj_lists = graph_to_adj_list(edges)
        self.assertEqual(adj_lists, {})


class TestShortestPathView(APITestCase, URLPatternsTestCase):
    urlpatterns = [
        path("shortest-path/", ShortestPathView.as_view(), name="shortest-path"),
    ]

    def setUp(self):
        self.node1 = Node.objects.create(pk=1, name="Node A")
        self.node2 = Node.objects.create(pk=2, name="Node B")
        self.node3 = Node.objects.create(pk=3, name="Node C")

        Edge.objects.create(source=self.node1, target=self.node2, weight=3)
        Edge.objects.create(source=self.node2, target=self.node3, weight=4)
        Edge.objects.create(source=self.node3, target=self.node1, weight=2)

    @override_settings(DEBUG=True)
    def test_shortest_path_valid_with_autonomy(self):
        data = {"sourceId": self.node1.pk, "targetId": self.node3.pk, "autonomy": 10}
        response = self.client.post(reverse("shortest-path"), data, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("distances", response.json())
        self.assertIn("path", response.json())

    @override_settings(DEBUG=True)
    def test_shortest_path_valid_without_autonomy(self):
        data = {
            "sourceId": self.node2.pk,
            "targetId": self.node1.pk,
        }
        response = self.client.post(reverse("shortest-path"), data, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("distances", response.json())
        self.assertIn("path", response.json())

    @override_settings(DEBUG=True)
    def test_shortest_path_missing_node(self):
        data = {
            "sourceId": 100,  # this node does not exist
            "targetId": self.node3.pk,
        }
        response = self.client.post(reverse("shortest-path"), data, format="json")

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
