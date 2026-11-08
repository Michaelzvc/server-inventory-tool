def display_servers(servers):
    if not servers:
        print("Inga servrar hittades.")
        return

    print()
    print(f"{'Namn':<15} {'Adress':<20} {'Miljö':<12} {'Roll':<20} {'Status':<10}")
    print("-" * 80) 


    for server in servers:
        print(
            f"{server['namn']:<15}" 
            f"{server['adress']:<20}" 
            f"{server['miljo']:<12}"
            f"{server['roll']:<20}" 
            f"{server['status']:<10}"
        )


def lagg_till_servrar(servrar, data_fil):
    namn = input("Ange servernamn: ")

    # Check if server name already exists
    for server in servrar:
        if server['namn'] == namn:
            print("En server med det namnet finns redan.")
            return

    adress = input("Ange serveradress: ")

    # validate environment
    while True:
        miljo = input("Ange servermiljö (dev, test, prod): ").lower()
        if miljo in ["dev", "test", "prod"]:
            break

        print("ogiltig miljö, skriv antingen 'dev', 'test', eller 'prod'.")


    roll = input("Ange serverroll: ")

    new_server = {
        "namn": namn,
        "adress": adress,
        "miljo": miljo,
        "roll": roll,
        "status": "okänd",  # Default status
        "senast_kontrollerad": ""
    }

    servrar.append(new_server)

    from lagring import save_servers
    save_servers(servrar, data_fil)

    print("Server tillagd och sparad.")

