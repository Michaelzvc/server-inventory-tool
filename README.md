# Server Inventory Tool

## Beskrivning
Server Inventory Tool är ett program som används för att hantera och kontrollera servrar. Programmet kan göra allt från att visa, lägga till, ta bort och filtrera servrar. Den kan även se om servrar är tillgängliga, samt att exportera informationen till CSV-filer.

## Krav
- Python 3
- Linux 
- Ping installerat

## Starta programmet

Starta den interaktiva menyn med:

```bash
python3 main.py
```

## Kommandoradsalternativ

Visa alla servrar:

```bash
python3 main.py --lista
```

Visa servrar beroende på miljö:

```bash
python3 main.py --lista --miljo prod
```

Kontrollera en specifik server:

```bash
python3 main.py --kontrollera web01
```

Kontrollera alla servrar:

```bash
python3 main.py --kontrollera-alla
```

Exportera alla servrar till CSV:

```bash
python3 main.py --export
```

Visa programmets hjälp:

```bash
python3 main.py --help
```

## Datafil

Programmet använder `servrar.json` för att lagra serverinformation

Det går att välja en annan datafil genom miljövariabeln `INVENTORY_DATAFIL`

Till exempel:

```bash
INVENTORY_DATAFIL=testdata.json python3 main.py
```

Om miljövariabeln inte anges används `servrar.json`

## Projektstruktur

- `main.py` – Startar programmet och hanterar kommandoradsargument
- `meny.py` – Hanterar den interaktiva menyn och funktioner för att visa, lägga till, ta bort och filtrera servrarna
- `lagring.py` – Hanterar inläsning och sparning av JSON samt export till CSV
- `kontroller.py` – Kontrollerar om servrar är tillgängliga med ping
- `servrar.json` – Innehåller information om servrarna
- `README.md` – Beskriver programmet och hur det används
- `REDOGORELSE.md` – Innehåller redogörelsen för uppgiften

## CSV-rapporter

Exporterade rapporter sparas automatiskt i katalogen `rapporter/`. Om den inte redan finns så skapas den 