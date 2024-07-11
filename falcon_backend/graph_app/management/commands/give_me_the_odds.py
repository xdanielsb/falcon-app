from django.core.management.base import BaseCommand

from graph_app.models import GraphMetadata, Edge, Empire, Node
from graph_app.types.empire import BountyHunterWithPlanetId
from graph_app.utils.db import load_initial_db, load_empire_info
from graph_app.utils.graph import graph_to_adj_list
from logic.best_path_heuristic import find_best_path_heuristic


def compute_odds(millennium_config: str, empire_config: str):
    load_initial_db(millennium_config)
    load_empire_info(empire_config)
    graph_info = GraphMetadata.objects.first()

    empire = Empire.objects.first()
    bounty_hunters_with_node_ids = []

    for bounty in empire.bounty_hunters.all():
        node = Node.objects.filter(name=bounty.planet).first()
        if node:
            bounty_hunters_with_node_ids.append(
                BountyHunterWithPlanetId(**{"day": bounty.day, "node_id": node.pk})
            )
    dis, path, stops, probability_arriving = find_best_path_heuristic(
        graph_info.source.pk,
        graph_info.target.pk,
        graph_to_adj_list(Edge.objects.all()),
        graph_info.autonomy,
        empire.countdown,
        bounty_hunters_with_node_ids,
    )

    return probability_arriving


class Command(BaseCommand):
    """
    Customer command to run the odds,  it receives the path to the millennium falcon configuration and the empire configuration
    instructions in the readme to run the command
    """

    help = (
        "Compute the odds of the millennium falcon arriving to the target destination"
    )

    def add_arguments(self, parser):
        parser.add_argument(
            "millennium-file-path",
            type=str,
            help="the path to the milleniun falcon configuration",
        )
        parser.add_argument(
            "empire-file-path",
            type=str,
            help="the path to the the empire configuration",
        )

    def handle(self, *args, **kwargs):
        millennium_config = kwargs["millennium-file-path"]
        empire_config = kwargs["empire-file-path"]
        probability_arriving = compute_odds(millennium_config, empire_config)
        print(f"\033[92mProbability computed: {probability_arriving}\033[0m")
