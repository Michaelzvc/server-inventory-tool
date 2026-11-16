import subprocess
from datetime import datetime
from lagring import spara_servrar


def kontrollera_server(servrar, servernamn, data_fil):
    for server in servrar:
        if server["namn"] == servernamn:

            try:
                resultat = subprocess.run(
                    ["ping", "-c", "1", server["adress"]],
                    capture_output=True,
                    text=True,
                    timeout=5
                )

                if resultat.returncode == 0:
                    server["status"] = "up"
                    print(f"Servern {servernamn} är tillgänglig.")
                else:
                    server["status"] = "down"
                    print(f"Servern {servernamn} är inte tillgänglig.")

            except subprocess.TimeoutExpired:
                server["status"] = "down"
                print(f"Servern {servernamn} svarade inte inom tidsgränsen.")

            server["senast_kontrollerad"] = datetime.now().strftime(
                "%Y-%m-%d %H:%M"
            )

            spara_servrar(servrar, data_fil)
            return

    print(f"Servern {servernamn} kunde inte hittas.")


def kontrollera_alla_servrar(servrar, data_fil):
    if not servrar:
        print("Det finns inga servrar att kontrollera.")
        return

    for server in servrar:
        kontrollera_server(servrar, server["namn"], data_fil)


            


    