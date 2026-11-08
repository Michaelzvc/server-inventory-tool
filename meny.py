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

    # Kontrollera om servernamnet redan finns
    for server in servrar:
        if server["namn"] == namn:
            print("En server med det namnet finns redan.")
            return

    adress = input("Ange serveradress: ")

    # Validera miljön
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

    from lagring import spara_servrar

    spara_servrar(servrar, datafil)

    print("Server tillagd och sparad.")
