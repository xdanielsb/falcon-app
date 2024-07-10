from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import graph_view, FindPathView, GraphInfoView

router = DefaultRouter()
urlpatterns = [
    path("", include(router.urls)),
    path("graph/", graph_view, name="graph"),
    path("find-path/", FindPathView.as_view(), name="find-path"),
    path("graph-info/", GraphInfoView.as_view(), name="graph-info"),
]
