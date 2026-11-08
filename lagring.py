import json
import os
from pathlib import Path


def hamta_servrar(datafil):
    filsokvag = Path(datafil)

    if filsokvag.exists():
        with open(filsokvag, "r", encoding="utf-8") as fil:
            servrar = json.load(fil)

        return servrar

    return []  # Returnera en tom lista om filen inte finns


def spara_servrar(servrar, datafil):
    filsokvag = Path(datafil)

    with open(filsokvag, "w", encoding="utf-8") as fil:
        json.dump(servrar, fil, indent=4, ensure_ascii=False)


def hamta_datafil():
    return os.environ.get("INVENTORY_DATAFIL", "servrar.json")
