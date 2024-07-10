import json
import os
from typing import Any


def make_absolute_path(path: str):
    if not os.path.isabs(path):
        current_dir = os.getcwd()
        absolute_path = os.path.join(current_dir, path)
        return absolute_path
    else:
        return path


def read_json_file(file_path) -> Any:
    # todo:  add tests
    try:
        with open(file_path, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"The file at {file_path} was not found.")
    except json.JSONDecodeError:
        print(f"The file at {file_path} does not contain valid JSON.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return None
