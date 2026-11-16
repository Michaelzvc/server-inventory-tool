import json
import os
import csv
from pathlib import Path
from datetime import datetime


def hamta_servrar(datafil):
    filsokvag = Path(datafil)

    if filsokvag.exists():
        with open(filsokvag, "r", encoding="utf-8") as fil:
            servrar = json.load(fil)

        return servrar

    return []  


def spara_servrar(servrar, datafil):
    filsokvag = Path(datafil)

    with open(filsokvag, "w", encoding="utf-8") as fil:
        json.dump(servrar, fil, indent=4, ensure_ascii=False)


def hamta_datafil():
    return os.environ.get("INVENTORY_DATAFIL", "servrar.json")


def exportera_csv(servrar):
    rapport_katalog = Path("rapporter")
    rapport_katalog.mkdir(exist_ok=True)

    tidpunkt = datetime.now().strftime("%Y-%m-%d_%H%M")
    filnamn = f"inventering_{tidpunkt}.csv"

    filsokvag = rapport_katalog / filnamn

    kolumner = [
        "namn",
        "adress",
        "miljo",
        "roll",
        "status",
        "senast_kontrollerad"
    ]

    with open(filsokvag, "w", newline="", encoding="utf-8") as fil:
        skrivare = csv.DictWriter(fil, fieldnames=kolumner)

        skrivare.writeheader()
        skrivare.writerows(servrar)

    print(f"Rapporten har sparats: {filsokvag}")