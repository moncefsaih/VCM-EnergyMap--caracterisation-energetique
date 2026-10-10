import os
import csv
from ultralytics import YOLO
from codecarbon import EmissionsTracker

nom_experience = "Video_Compressee_CRF35"

# 1. On charge la petite intelligence artificielle de base
model = YOLO("yolov8n.pt")

# 2. Copie-colle ici le chemin d'UNE image qui se trouve dans ton dossier téléchargé
chemin_de_mon_fichier = r"C:\SDA\M3\TDM\video_compressee.mp4"

# 3. On allume le compteur d'énergie juste avant l'effort !
tracker = EmissionsTracker()
tracker.start()

# 4. L'ordinateur fait son calcul (l'inférence)
resultats = model.predict(source=chemin_de_mon_fichier, show=True, save=True)

# 5. On arrête le compteur juste après l'effort
emissions = tracker.stop()

# --- COLLECTE AUTOMATIQUE DES DONNÉES ---
# Calcul de la taille du fichier en Kilo-octets (Ko) pour le "Débit"
taille_fichier_ko = os.path.getsize(chemin_de_mon_fichier) / 1024

# Récupération des temps de calcul moyens (en millisecondes)
temps_pre_traitement = resultats[0].speed['preprocess']
temps_inference = resultats[0].speed['inference']

# --- SAUVEGARDE DANS LE FICHIER EXCEL (CSV) ---
nom_fichier_csv = "resultats_experiences.csv"
fichier_existe = os.path.isfile(nom_fichier_csv)

with open(nom_fichier_csv, mode='a', newline='') as fichier:
    writer = csv.writer(fichier, delimiter=';')
    
    # Si le fichier est nouveau, on crée la ligne d'en-tête (les titres des colonnes)
    if not fichier_existe:
        writer.writerow(["Nom de l'experience", "Taille fichier (Ko)", "Temps Pre-traitement (ms)", "Temps Inference (ms)", "Energie totale (kWh)"])
    
    # On ajoute la ligne avec tous tes résultats !
    writer.writerow([nom_experience, round(taille_fichier_ko, 2), round(temps_pre_traitement, 2), round(temps_inference, 2), emissions])

print(f"\n✅ Analyse terminée ! Les résultats ont été sauvegardés dans le fichier : {nom_fichier_csv}")

# 6. On affiche le résultat de l'énergie consommée
print(f"L'énergie totale consommée est de : {emissions} kWh")

input("Appuie sur Entrée pour fermer...")