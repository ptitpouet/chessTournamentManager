# chessTournamentManager
Projet 3 - Développez un programme logiciel en Python
https://github.com/ptitpouet/chessTournamentManager.git
Auteur : Thierry Moncorger pour Openclassrooms.com

# Présentation
Cet outil est un gestionnaire de Tournoi d'échecs. 
- Il permet de gérer une base de données de joueurs
- Il permet de créer ses tournois
- Les matchs sont générés selon la regle du systeme-suisse
- Les tournois lancés peuvent être repris à tout moment
- Une section dédiée à l'édition de différents rapports


# Liste des dépendences
[requirements.txt](requirements.txt) contient les dépendences pour la mise en place de l'environnement virtuel.

# Création de votre environnement virtuel 
    $ python -m venv <environment name>
# Activation de l'environnement virtuel
    .\<environment name>\Scripts\activate.bat
# Installer les fichiers du requirements.txt
    pip install -r requirements.txt       
# Lancer le programme
    $ py main.py


# La base de données
Le fichier db.json contient l'ensemble de la base de données du logiciel


# Vérification du code et son respect de la norme PEP8
Le plugin Flake8 permet de générer des rapports html des violations de la norme PEP8
- Installation :
$ pip install flake8-html
- Exécution :
$ flake8 --format=html --htmldir=<Nomdudossier>