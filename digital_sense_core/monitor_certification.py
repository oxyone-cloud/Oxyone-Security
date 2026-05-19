import time
import requests
from datetime import datetime

# CONFIGURATION SSCI - PROTECTION CONVENTION DE BERNE
DB_URL = "https://digitalsense-5a6f2-default-rtdb.firebaseio.com/tracking.json"
LOG_FILE = "rapport_conformite_ssci.txt"

def certifier_et_archiver():
    print("--- PROTOCOLE DIGITAL SENSE : ARCHIVAGE ACTIF ---")
    
    with open(LOG_FILE, "a") as f:
        f.write(f"\n--- SESSION DU {datetime.now().strftime('%Y-%m-%d')} ---\n")
        f.write("Propriété exclusive de SSCI - Certification OxyONE\n")

    while True:
        try:
            response = requests.get(DB_URL)
            data = response.json()
            
            if data and "camion_01" in data:
                temp = data["camion_01"]["temp"]
                timestamp = datetime.now().strftime("%H:%M:%S")
                certif = "VALIDE" if temp < -18 else "ALERTE"
                
                log_entry = f"[{timestamp}] Temp: {temp}C | Statut: {certif} | Signé: SSCI_DS_PRO\n"
                
                # Affichage console
                print(log_entry.strip())
                
                # Écriture dans le rapport (Preuve de conformité)
                with open(LOG_FILE, "a") as f:
                    f.write(log_entry)
            
            time.sleep(10) # Archivage toutes les 10 secondes pour un rapport dense
        except Exception as e:
            print(f"Erreur : {e}")
            break

if __name__ == "__main__":
    certifier_et_archiver()
