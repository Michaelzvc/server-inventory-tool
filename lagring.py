import json
import os
from pathlib import Path


def load_servers(data_file):
    data_path = Path(data_file)

    if data_path.exists():
        with open(data_path, "r", encoding="utf-8") as file:
            servers = json.load(file)

        return servers 

    return []  # Return an empty list if the file does not exist


def save_servers(servers, data_file):
    data_path = Path(data_file)

    with open(data_path, "w", encoding="utf-8") as file:
        json.dump(servers, file, indent=4, ensure_ascii=False)


def get_data_file():
    return os.environ.get("INVENTORY_DATAFIL", "servrar.json")

