from django.test import override_settings
from django.urls import path, reverse
from rest_framework import status
from rest_framework.test import APITestCase, URLPatternsTestCase

from graph_app.views import CreateGraphView


class TestGraphInfoPathView(APITestCase, URLPatternsTestCase):
    urlpatterns = [
        path("create-graph/", CreateGraphView.as_view(), name="create-graph"),
    ]

    @override_settings(DEBUG=True)
    def test_get_graph_info(self):
        response = self.client.post(reverse("create-graph"), {"random": True})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # check that the method create random graph was called
