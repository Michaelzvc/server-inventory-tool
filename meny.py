from lagring import spara_servrar, exportera_csv
from kontroller import kontrollera_server, kontrollera_alla_servrar


def visa_servrar(servrar):
    if not servrar:
        print("Inga servrar hittades.")
        return

    print()
    print(f"{'Namn':<15} {'Adress':<20} {'Miljö':<12} {'Roll':<20} {'Status':<10}")
    print("-" * 80)

    for server in servrar:
        print(
            f"{server['namn']:<15}"
            f"{server['adress']:<20}"
            f"{server['miljo']:<12}"
            f"{server['roll']:<20}"
            f"{server['status']:<10}"
        )


def lagg_till_servrar(servrar, datafil):
    namn = input("Ange servernamn: ")

    
    for server in servrar:
        if server["namn"] == namn:
            print("En server med det namnet finns redan.")
            return

    adress = input("Ange serveradress: ")

    
    while True:
        miljo = input("Ange servermiljö (dev, test, prod): ").lower()
        if miljo in ["dev", "test", "prod"]:
            break

        print("Ogiltig miljö, skriv antingen 'dev', 'test' eller 'prod'.")

    roll = input("Ange serverroll: ")

    ny_server = {
        "namn": namn,
        "adress": adress,
        "miljo": miljo,
        "roll": roll,
        "status": "unknown",
        "senast_kontrollerad": "",
    }

    servrar.append(ny_server)
    spara_servrar(servrar, datafil)

    print("Server tillagd och sparad.")


def ta_bort_server(servrar, data_fil):
    namn = input("Ange namnet på servern du vill ta bort: ")

    for server in servrar:
        if server["namn"] == namn:

            if server["miljo"] == "prod":
                bekraftelse = input(
                    "Du försöker ta bort en produktionsserver. Är du säker? (ja/nej): "
                ).lower()

                if bekraftelse != "ja":
                    print("Borttagning avbruten.")
                    return

            servrar.remove(server)

            spara_servrar(servrar, data_fil)

            print("Servern har tagits bort.")
            return

    print("Server hittades inte.")


def filtrera_servrar(servrar):
    while True:
        miljo = input("Ange miljö att filtrera på (dev, test, prod): ").lower()

        if miljo in ["dev", "test", "prod"]:
            break

        print("Ogiltig miljö, vänligen försök igen.")

    filtrerade_servrar = []

    for server in servrar:
        if server["miljo"] == miljo:
            filtrerade_servrar.append(server)

    print(f"\nServrar i miljön '{miljo}':")
    visa_servrar(filtrerade_servrar)


def visa_meny(servrar, data_fil):
    while True:
        print("\n===== SERVER INVENTORY TOOL =====")
        print("1. Visa alla servrar")
        print("2. Filtrera servrar efter miljö")
        print("3. Lägg till server")
        print("4. Ta bort server")
        print("5. Kontrollera en server")
        print("6. Kontrollera alla servrar")
        print("7. Exportera till CSV")
        print("8. Avsluta")

        val = input("\nVälj ett alternativ: ")

        if val == "1":
            visa_servrar(servrar)

        elif val == "2":
            filtrera_servrar(servrar)

        elif val == "3":
            lagg_till_servrar(servrar, data_fil)

        elif val == "4":
            ta_bort_server(servrar, data_fil)

        elif val == "5":
            namn = input("Ange servernamn: ")
            kontrollera_server(servrar, namn, data_fil)

        elif val == "6":
            kontrollera_alla_servrar(servrar, data_fil)

        elif val == "7":
            exportera_csv(servrar)

        elif val == "8":
            print("Programmet avslutas.")
            break

        else:
            print("Ogiltigt val. Försök igen.")
            

    

        