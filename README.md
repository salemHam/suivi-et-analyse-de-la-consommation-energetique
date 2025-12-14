# suivi-et-analyse-de-la-consommation-energetique

Guide étape par étape pour installer l'environnement, vérifier la qualité, lancer les tests et exécuter le script principal.

## Prérequis

- Python 3.13 recommandé .
- Un compte MongoDB et une URI valide.


## 1) Installer Python (idéalement 3.13)

- Téléchargez Python : https://www.python.org/downloads/
- Cochez « Add Python to PATH » pendant l'installation.
- Vérifiez l'installation:

```powershell
python --version
```

## 2) Créer un environnement virtuel (venv)

Depuis le dossier du projet:

```powershell

python -m venv .venv

# Activer (PowerShell)
\.\.venv\Scripts\Activate.ps1

# (CMD)
\.\.venv\Scripts\activate.bat

# (Git Bash / linux)
source .venv/Scripts/activate
```

## 3) Installer les dépendances

```powershell
pip install --upgrade pip
pip install -r requirements.txt
```



## 4) Configurer l'URI MongoDB

créer un fichier env.py et ajouter votre uri mongodb
# fichier: env.py
db_user_name = "votre_utilisateur"
db_password = "votre_mot_de_passe"
uri = f"mongodb+srv://{db_user_name}:{db_password}@<votre-cluster>.mongodb.net/?appName=<VotreApp>"



## 5) Vérifier la qualité du code (flake8)

```powershell
flake8 .
```

- Les règles sont paramétrées dans `.flake8` .


## 6) Lancer les tests (pytest)

```powershell
pytest
```



## 7) Exécuter le script principal

```powershell
python main.py
```

Fonctionnement attendu:

- Connexion à MongoDB (message « Pinged your deployment… » si OK).
- Lecture simulée des capteurs (10 itérations).
- Détection et affichage des anomalies (rouge).
- Sauvegarde des enregistrements dans MongoDB (ID en vert).
- Sauvegarde de l'historique de facturation càd tous les 3 mois.


## Arborescence utile

- Code applicatif: `src/` (`sensor.py`, `anomaly.py`, `database.py`, `const.py`).
- Script d'entrée: `main.py`.
- Configuration MongoDB: `env.py`.
- Qualité/tests: `.flake8`, `tests/`.
