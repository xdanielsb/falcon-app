from django.test import override_settings
from django.urls import path, reverse
from rest_framework import status
from rest_framework.test import APITestCase, URLPatternsTestCase

from graph_app.models import Node, Edge
from graph_app.views import graph_view


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
