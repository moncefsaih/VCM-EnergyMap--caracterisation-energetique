# S5 — VCM-EnergyMap : Caractérisation Énergétique

## Objectif du projet
Ce projet propose une cartographie expérimentale et reproductible du coût énergétique d'une chaîne VCM (Video Coding for Machines). Il vise à répondre à la question suivante : **Comment le point de fonctionnement d’une chaîne VCM influence-t-il la précision de la tâche, le débit, le temps et l’énergie ?**

L'hypothèse testée est que le point de fonctionnement minimisant le débit ne minimise pas nécessairement l’énergie totale à une précision acceptable.

## Description matérielle et logicielle
- **Système d'exploitation** : Windows 10
- **Processeur (CPU / GPU intégré)** : Intel Core i7-8650U (Intel UHD Graphics)
- **Outils utilisés** : Python 3, FFmpeg, Git
- **Modèle IA figé** : YOLOv8 nano (`yolov8n.pt`)
- **Mesure d'énergie** : CodeCarbon (estimation logicielle basée sur le processeur)

## Prérequis et Installation
Pour reproduire ces expériences, vous devez installer les outils suivants :

1. **Installer FFmpeg (Encodeur)** :
   Ouvrez PowerShell et tapez :
   `winget install ffmpeg`
   (Redémarrez le terminal après l'installation).

2. **Installer les bibliothèques Python** :
   `pip install ultralytics codecarbon`

## Reproduction des expériences

### 1. Préparation des données (Niveaux de compression)
Téléchargez une vidéo de test (ex: `person-bicycle-car-detection.mp4`). Utilisez FFmpeg pour générer différents points de fonctionnement (variation du QP) :

- **Haute qualité (CRF 15)** :
  `ffmpeg -i person-bicycle-car-detection.mp4 -vcodec libx264 -crf 15 video_haute_qualite.mp4`
- **Basse qualité (CRF 45)** :
  `ffmpeg -i person-bicycle-car-detection.mp4 -vcodec libx264 -crf 45 video_basse_qualite.mp4`

### 2. Exécution des mesures
Dans le fichier `test.py`, modifiez les variables `nom_experience` et `chemin_de_mon_fichier` pour pointer vers la vidéo à tester.

Lancez le script :
`python test.py`

### 3. Résultats (Logs bruts)
Le script va automatiquement générer et mettre à jour un fichier `resultats_experiences.csv`. Ce fichier contient les logs bruts nécessaires pour tracer les figures :
- Débit (Taille du fichier en Ko)
- Temps de prétraitement et d'inférence (ms)
- Énergie totale estimée (kWh)