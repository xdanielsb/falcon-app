from rest_framework.decorators import api_view
from rest_framework.response import Response

from graph_app.models import Node, Edge
from graph_app.serializers import NodeSerializer, EdgeSerializer


@api_view(["GET"])
def graph_view(request):
    nodes = Node.objects.all()
    edges = Edge.objects.all()

    node_serializer = NodeSerializer(nodes, many=True, context={"request": request})
    edge_serializer = EdgeSerializer(edges, many=True, context={"request": request})

    return Response({"nodes": node_serializer.data, "edges": edge_serializer.data})
