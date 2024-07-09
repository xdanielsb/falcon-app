from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework import views
from rest_framework.decorators import api_view
from rest_framework.response import Response

from graph_app.models import Node, Edge
from graph_app.serializers import NodeSerializer, EdgeSerializer
from graph_app.utils import graph_to_adj_list
from logic.shortest_path import get_shortest_path_with_autonomy


@api_view(["GET"])
def graph_view(request):
    """
    Returns all nodes and edges in the graph
    """
    nodes = Node.objects.all()
    edges = Edge.objects.all()

    node_serializer = NodeSerializer(nodes, many=True, context={"request": request})
    edge_serializer = EdgeSerializer(edges, many=True, context={"request": request})

    return Response({"nodes": node_serializer.data, "edges": edge_serializer.data})


class ShortestPathView(views.APIView):
    def post(self, request):
        source = get_object_or_404(Node, pk=request.data["sourceId"])
        target = get_object_or_404(Node, pk=request.data["targetId"])
        autonomy = request.data.get("autonomy", None)

        dis, path = get_shortest_path_with_autonomy(
            source.pk, target.pk, graph_to_adj_list(Edge.objects.all()), autonomy
        )
        return JsonResponse({"distances": dis, "path": path})
