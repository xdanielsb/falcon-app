from rest_framework import serializers

from .models import Node, Edge


class NodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Node
        fields = ["pk", "name"]


class EdgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Edge
        fields = ["source", "target", "weight"]
