from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import graph_view, ShortestPathView, GraphInfoView

router = DefaultRouter()
urlpatterns = [
    path("", include(router.urls)),
    path("graph/", graph_view, name="graph"),
    path("shortest-path/", ShortestPathView.as_view(), name="shortest-path"),
    path("graph-info/", GraphInfoView.as_view(), name="graph-info"),
]
