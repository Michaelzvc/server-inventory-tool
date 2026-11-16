import argparse
from lagring import hamta_servrar, hamta_datafil
from meny import visa_meny, visa_servrar


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

    argument = parser.parse_args()

    data_fil = hamta_datafil()
    servrar = hamta_servrar(data_fil)

    if argument.lista:
        if argument.miljo:
            filtrerade_servrar = []

            for server in servrar:
                if server["miljo"] == argument.miljo:
                    filtrerade_servrar.append(server)

            visa_servrar(filtrerade_servrar)
        else:
            visa_servrar(servrar)

    else:
        visa_meny(servrar, data_fil)


if __name__ == "__main__":
    main()