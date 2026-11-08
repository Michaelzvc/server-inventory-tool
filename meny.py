def display_servers(servers):
    if not servers:
        print("No servers found.")
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