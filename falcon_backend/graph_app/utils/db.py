import os
import sqlite3
from contextlib import closing

from dotenv import dotenv_values

from falcon_backend.logger import get_logger
from graph_app.models import Node, Edge, GraphMetadata, Empire, BountyHunter
from graph_app.types.empire import EmpireSchema
from graph_app.types.path import PathInfo, PathInfoSchema
from graph_app.utils.file import read_json_file, make_absolute_path


def get_or_create_node(name: str) -> Node:
    try:
        node = Node.objects.get(name=name)
        return node
    except Node.DoesNotExist:
        node = Node.objects.create(name=name)
        return node


def load_metadata(metadata_path: str) -> PathInfo:
    data = read_json_file(metadata_path)
    schema = PathInfoSchema()
    route_info = schema.load(data)
    return route_info


def load_nodes_and_edges(metadata_path: str) -> None:
    # Check if database file exists
    db_file = load_metadata(metadata_path).routes_db
    # if relative
    db_path = os.getcwd() + "/" + os.path.dirname(metadata_path) + "/" + db_file
    # todo: if absolute and write tests

    if not os.path.exists(db_path):
        get_logger().error(f"Database file not found: {db_path}")
        raise FileNotFoundError(f"Database file not found: {db_path}")

    # Clear existing data
    Node.objects.all().delete()
    Edge.objects.all().delete()

    # Load data from database
    with closing(sqlite3.connect(db_path)) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT origin, destination, travel_time FROM routes; ")

        for row in cursor:
            origin_str, destination_str, travel_time = row
            origin = get_or_create_node(origin_str)
            target = get_or_create_node(destination_str)
            Edge.objects.create(source=origin, target=target, weight=travel_time)

    get_logger().info("Nodes and edges loaded")


def load_graph_metadata(metadata_path: str) -> None:
    """
    load the metadata of the graph, each time clean the previous data:w
    """
    metadata = load_metadata(metadata_path)
    source = get_or_create_node(metadata.departure)
    target = get_or_create_node(metadata.arrival)
    # Clear existing data
    GraphMetadata.objects.all().delete()
    GraphMetadata.objects.create(
        source=source, target=target, autonomy=metadata.autonomy
    )
    get_logger().info("Graph metadata loaded")


def load_initial_db(path: str | None = None) -> None:
    """
    load the initial database configuration given the path of a file store in the value of an .env variable
    """
    config = dotenv_values(".env")
    if path is not None:
        path_configuration = path
    else:
        path_configuration = config["MILLENNIUM_FALCON_PATH"]

    if not path_configuration:
        get_logger().error("MILLENNIUM_FALCON_PATH not found in .env")
        raise ValueError("MILLENNIUM_FALCON_PATH not found in .env")

    absolute_path = make_absolute_path(path_configuration)
    if not os.path.exists(absolute_path):
        get_logger().error(f"Configuration file not found: {absolute_path}")
        raise FileNotFoundError(f"Configuration file not found: {absolute_path}")

    load_nodes_and_edges(path_configuration)
    load_graph_metadata(path_configuration)


def load_empire_info(path: str | None = None) -> None:
    """
    load the empire information
    """
    config = dotenv_values(".env")

    if path is not None:
        path_configuration = path
    else:
        path_configuration = config["EMPIRE_PATH"]

    if not path_configuration:
        get_logger().error("EMPIRE_PATH not found in .env")
        raise ValueError("EMPIRE_PATH not found in .env")

    absolute_path = make_absolute_path(path_configuration)
    if not os.path.exists(absolute_path):
        get_logger().error(f"Configuration file not found: {absolute_path}")
        raise FileNotFoundError(f"Configuration file not found: {absolute_path}")
    # verify schema
    data = read_json_file(absolute_path)
    schema = EmpireSchema()
    empire_info = schema.load(data)
    # cleaning
    BountyHunter.objects.all().delete()
    Empire.objects.all().delete()
    # loading in the database
    empire = Empire.objects.create(countdown=empire_info.countdown)

    for bh_data in empire_info.bounty_hunters:
        bounty_hunter = BountyHunter.objects.create(
            planet=bh_data.planet, day=bh_data.day
        )
        empire.bounty_hunters.add(bounty_hunter)

    get_logger().info("Empire info loaded")
