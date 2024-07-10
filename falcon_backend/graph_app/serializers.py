from rest_framework import serializers

from .models import Node, Edge, BountyHunter


class NodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Node
        fields = ["pk", "name"]


class EdgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Edge
        fields = ["pk", "source", "target", "weight"]


class BountyHunterSerializer(serializers.ModelSerializer):
    class Meta:
        model = BountyHunter
        fields = ["day", "planet"]
