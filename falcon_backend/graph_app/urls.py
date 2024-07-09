from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import graph_view

router = DefaultRouter()
urlpatterns = [
    path("", include(router.urls)),
    path("graph/", graph_view, name="graph"),
]
