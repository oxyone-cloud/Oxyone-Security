import os
import time
from datetime import datetime

# Configuration du fichier à surveiller
FICHIER_CIBLE = "index.html"
FICHIER_LOGS = "security_alerts.log"

def surveiller():
    print(f"🛡️ Surveillance activée sur : {FICHIER_CIBLE}")
    # On récupère l'heure de la dernière modification au démarrage
    derniere_modif = os.path.getmtime(FICHIER_CIBLE)

    while True:
        try:
            # Vérification de l'état actuel du fichier
            actuelle_modif = os.path.getmtime(FICHIER_CIBLE)
            
            if actuelle_modif != derniere_modif:
                message = f"⚠️ ALERTE : Modification suspecte le {datetime.now()}\n"
                print(message)
                
                # Écriture dans le journal de sécurité
                with open(FICHIER_LOGS, "a") as f:
                    f.write(message)
                
                # Mise à jour de l'état
                derniere_modif = actuelle_modif
            
            time.sleep(1) # Vérification chaque seconde
        except FileNotFoundError:
            print("❌ Erreur : Le fichier index.html est introuvable !")
            break

if __name__ == "__main__":
    surveiller()
