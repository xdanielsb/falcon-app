import os
import sqlite3
from contextlib import closing

from dotenv import dotenv_values

from graph_app.models import Node, Edge, GraphMetadata
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


def load_graph_metadata(metadata_path: str) -> None:
    metadata = load_metadata(metadata_path)
    source = get_or_create_node(metadata.departure)
    target = get_or_create_node(metadata.arrival)
    # Clear existing data
    GraphMetadata.objects.all().delete()
    GraphMetadata.objects.create(
        source=source, target=target, autonomy=metadata.autonomy
    )


def load_initial_db() -> None:
    """
    load the initial database configuration given the path of a file store in the value of an .env variable
    """
    config = dotenv_values(".env")
    path_configuration = config["MILLENNIUM_FALCON_PATH_INITIAL_CONFIGURATION"]
    if not path_configuration:
        raise ValueError(
            "MILLENNIUM_FALCON_PATH_INITIAL_CONFIGURATION not found in .env"
        )

    absolute_path = make_absolute_path(path_configuration)
    if not os.path.exists(absolute_path):
        raise FileNotFoundError(f"Configuration file not found: {absolute_path}")

    load_nodes_and_edges(path_configuration)
    load_graph_metadata(path_configuration)
