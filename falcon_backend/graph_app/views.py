from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework import views
from rest_framework.decorators import api_view
from rest_framework.response import Response

from falcon_backend.logger import get_logger
from graph_app.models import Node, Edge, Empire, GraphMetadata, BountyHunter
from graph_app.serializers import NodeSerializer, EdgeSerializer, BountyHunterSerializer
from graph_app.types.empire import BountyHunterWithPlanetId
from graph_app.utils.graph import graph_to_adj_list
from logic.best_path_heuristic import find_best_path_heuristic


# endpoints logic


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


class FindPathView(views.APIView):
    def post(self, request):
        source = get_object_or_404(Node, pk=request.data["sourceId"])
        target = get_object_or_404(Node, pk=request.data["targetId"])
        autonomy = request.data.get("autonomy", None)

        empire = Empire.objects.first()
        bounty_hunters_with_node_ids = []

        for bounty in empire.bounty_hunters.all():
            node = Node.objects.filter(name=bounty.planet).first()
            if node:
                bounty_hunters_with_node_ids.append(
                    BountyHunterWithPlanetId(**{"day": bounty.day, "node_id": node.pk})
                )

        dis, path, stops, probability_arriving = find_best_path_heuristic(
            source.pk,
            target.pk,
            graph_to_adj_list(Edge.objects.all()),
            autonomy,
            empire.countdown,
            bounty_hunters_with_node_ids,
        )
        get_logger().info(f"Probability computed: {probability_arriving}")
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
