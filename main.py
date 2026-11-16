import argparse
import sys
from lagring import hamta_servrar, hamta_datafil, exportera_csv
from meny import visa_meny, visa_servrar
from kontroller import kontrollera_server, kontrollera_alla_servrar


def main():
    parser = argparse.ArgumentParser(
        description="Verktyg för att hantera servrar."
    )

    parser.add_argument(
        "--lista",
        action="store_true",
        help="Visa alla servrar."
    )

    parser.add_argument(
        "--miljo",
        choices=["dev", "test", "prod"],
        help="Filtrera servrar efter miljö."
    )

    parser.add_argument(
        "--kontrollera",
        help="Kontrollera en specifik server."
    )

    parser.add_argument(
        "--kontrollera-alla",
        action="store_true",
        help="Kontrollera alla servrar."
    )

    parser.add_argument(
    "--export",
    action="store_true",
    help="Exportera alla servrar till CSV."
    )

    argument = parser.parse_args()

    data_fil = hamta_datafil()
    servrar = hamta_servrar(data_fil)

    if argument.kontrollera:
        kontrollera_server(servrar, argument.kontrollera, data_fil)

        hittad = False

        for server in servrar:
            if server["namn"] == argument.kontrollera:
                hittad = True

                if server["status"] == "down":
                    sys.exit(1)

        if not hittad:
            sys.exit(1)

    elif argument.kontrollera_alla:
        kontrollera_alla_servrar(servrar, data_fil)

        for server in servrar:
            if server["status"] == "down":
                sys.exit(1)

    elif argument.lista:
        if argument.miljo:
            filtrerade_servrar = []

            for server in servrar:
                if server["miljo"] == argument.miljo:
                    filtrerade_servrar.append(server)

            visa_servrar(filtrerade_servrar)
        else:
            visa_servrar(servrar)

    elif argument.export:
        exportera_csv(servrar)

    else:
        visa_meny(servrar, data_fil)
        

if __name__ == "__main__":
    main()