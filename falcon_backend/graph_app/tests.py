from django.test import override_settings
from django.urls import path, reverse
from rest_framework import status
from rest_framework.test import APITestCase, URLPatternsTestCase

from graph_app.views import graph_view


class APIGraphTests(APITestCase, URLPatternsTestCase):
    urlpatterns = [
        path("graph/", graph_view, name="graph"),
    ]

    @override_settings(DEBUG=True)
    def test_get_graph(self):
        response = self.client.get(reverse("graph"), format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {"nodes": [], "edges": []})
