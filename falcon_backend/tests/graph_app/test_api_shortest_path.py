from django.test import override_settings
from django.urls import path, reverse
from rest_framework import status
from rest_framework.test import APITestCase, URLPatternsTestCase

from graph_app.models import Edge, Node
from graph_app.views import ShortestPathView


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
