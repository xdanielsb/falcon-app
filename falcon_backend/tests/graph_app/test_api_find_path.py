from django.test import override_settings
from django.urls import path, reverse
from rest_framework import status
from rest_framework.test import APITestCase, URLPatternsTestCase

from graph_app.models import Edge, Node, BountyHunter, Empire
from graph_app.views import FindPathView


class TestFindPathView(APITestCase, URLPatternsTestCase):
    urlpatterns = [
        path("find-path/", FindPathView.as_view(), name="find-path"),
    ]

    def setUp(self):
        self.node1 = Node.objects.create(pk=1, name="Node A")
        self.node2 = Node.objects.create(pk=2, name="Node B")
        self.node3 = Node.objects.create(pk=3, name="Node C")

        self.edge1 = Edge.objects.create(source=self.node1, target=self.node2, weight=3)
        self.edge2 = Edge.objects.create(source=self.node2, target=self.node3, weight=4)
        self.edge3 = Edge.objects.create(source=self.node3, target=self.node1, weight=2)

        empire = Empire.objects.create(countdown=10)
        self.bounty_hunter_1 = BountyHunter.objects.create(day=1, planet="Node A")
        self.bounty_hunter_2 = BountyHunter.objects.create(day=1, planet="Node B")
        empire.bounty_hunters.add(self.bounty_hunter_1)
        empire.bounty_hunters.add(self.bounty_hunter_2)

    @override_settings(DEBUG=True)
    def test_find_path_valid_with_autonomy(self):
        data = {"sourceId": self.node1.pk, "targetId": self.node3.pk, "autonomy": 100}
        response = self.client.post(reverse("find-path"), data, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        res = response.json()
        assert res["distances"][str(self.node3.pk)] == 2
        assert sorted(res["path"]) == [self.node1.pk, self.node3.pk]

    @override_settings(DEBUG=True)
    def test_find_path_valid_without_autonomy(self):
        data = {
            "sourceId": self.node2.pk,
            "targetId": self.node1.pk,
        }
        response = self.client.post(reverse("find-path"), data, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("distances", response.json())
        self.assertIn("path", response.json())
        self.assertIn("probability", response.json())

    @override_settings(DEBUG=True)
    def test_find_path_missing_node(self):
        data = {
            "sourceId": 100,  # this node does not exist
            "targetId": self.node3.pk,
        }
        response = self.client.post(reverse("find-path"), data, format="json")

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    @override_settings(DEBUG=True)
    def test_autonomy_is_lower_than_minimun_distance(self):
        data = {"sourceId": self.node1.pk, "targetId": self.node3.pk, "autonomy": 0}
        response = self.client.post(reverse("find-path"), data, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.json(), {"distances": None, "path": None, "probability": 0}
        )
