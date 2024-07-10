from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework import views
from rest_framework.decorators import api_view
from rest_framework.response import Response

from graph_app.models import Node, Edge, Empire, GraphMetadata, BountyHunter
from graph_app.serializers import NodeSerializer, EdgeSerializer, BountyHunterSerializer
from graph_app.utils.graph import graph_to_adj_list
from logic.probability_arriving import compute_probability_arrival
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
        empire = Empire.objects.first()
        probability_arriving = compute_probability_arrival(
            target.pk, (dis, autonomy), empire
        )
        return JsonResponse(
            {"distances": dis, "path": path, "probability": probability_arriving}
        )


class GraphInfoView(views.APIView):
    def get(self, request):
        graph_info = GraphMetadata.objects.first()
        empire = Empire.objects.first()
        hunters = BountyHunter.objects.all()
        bounty_hunters = BountyHunterSerializer(
            hunters, many=True, context={"request": request}
        ).data
        return Response(
            {
                "numberOfNodes": Node.objects.count(),
                "numberOfEdges": Edge.objects.count(),
                "hunters": bounty_hunters,
                "countDown": empire.countdown,
                "sourceId": graph_info.source.pk,
                "targetId": graph_info.target.pk,
                "autonomy": graph_info.autonomy,
            }
        )
