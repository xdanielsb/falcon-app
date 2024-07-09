from django.db import models


class Node(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        indexes = [models.Index(fields=["name"])]


class Edge(models.Model):
    source = models.ForeignKey(
        Node, on_delete=models.CASCADE, related_name="source_node"
    )
    destination = models.ForeignKey(
        Node, on_delete=models.CASCADE, related_name="destination_node"
    )
    weight = models.IntegerField()

    def __str__(self):
        return f"{self.source.name} -> {self.destination.name} : {self.weight}"
