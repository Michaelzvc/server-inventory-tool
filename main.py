from lagring import hamta_servrar, hamta_datafil
from meny import visa_meny


def main():
    data_fil = hamta_datafil()
    servrar = hamta_servrar(data_fil)

    visa_meny(servrar, data_fil)


if __name__ == "__main__":
    main() 