from django.test import override_settings
from django.urls import path, reverse
from rest_framework import status
from rest_framework.test import APITestCase, URLPatternsTestCase

from graph_app.models import Edge, Node, BountyHunter, Empire, GraphMetadata
from graph_app.views import ShortestPathView, GraphInfoView


class TestGraphInfoPathView(APITestCase, URLPatternsTestCase):
    urlpatterns = [
        path("graph-info/", GraphInfoView.as_view(), name="graph-info"),
    ]

    def setUp(self):
        self.node1 = Node.objects.create(pk=1, name="Node A")
        self.node2 = Node.objects.create(pk=2, name="Node B")
        self.node3 = Node.objects.create(pk=3, name="Node C")

        Edge.objects.create(source=self.node1, target=self.node2, weight=3)
        Edge.objects.create(source=self.node2, target=self.node3, weight=4)
        Edge.objects.create(source=self.node3, target=self.node1, weight=2)
        self.graph_meta = GraphMetadata.objects.create(source=self.node1, target=self.node3, autonomy=10)

        self.empire = Empire.objects.create(countdown=10)
        bounty_hunter = BountyHunter.objects.create(day=1, planet="Marz")
        self.empire.bounty_hunters.add(bounty_hunter)

    @override_settings(DEBUG=True)
    def test_get_graph_info(self):
        response = self.client.get(reverse("graph-info"))
        expected_response = {
          'targetId': self.graph_meta.target.pk,
          'autonomy': self.graph_meta.autonomy,
          'countDown': self.empire.countdown,
          'sourceId': self.graph_meta.source.pk,
          'hunters': [{'day': 1, 'planet': 'Marz'}],
          'numberOfEdges': 3,
          'numberOfNodes': 3
        }
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(expected_response, response.data)

