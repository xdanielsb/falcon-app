import json
import os
from typing import Any

from falcon_backend.logger import get_logger


def make_absolute_path(path: str):
    if not os.path.isabs(path):
        current_dir = os.getcwd()
        absolute_path = os.path.join(current_dir, path)
        return absolute_path
    else:
        return path


def read_json_file(file_path) -> Any:
    try:
        with open(file_path, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        get_logger().error(f"The file at {file_path} was not found.")
    except json.JSONDecodeError:
        get_logger().error(f"The file at {file_path} does not contain valid JSON.")
    except Exception as e:
        get_logger().error(f"An error occurred: {e}")
    return None
