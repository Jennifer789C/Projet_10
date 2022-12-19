# OpenClassRooms - Python - Projet 10 : SoftDesk

Ce projet consiste à créer une API RESTful où les utilisateurs stockeront des 
données concernant des projets d'applications :  
<!-- 2 espaces à la fin de la ligne pour un saut de ligne -->
	- utilisation du framework Django,
	- utilisation du framework Django REST,
    - utilisation du package drf-nested-routers pour combiner des routeurs,
	- mise en place de différents endpoints personnalisés,  
	- mise en place de permissions personnalisées,  
    - rédaction d'une documentation précise,  
    - respect des normes OWASP et RGPD.


## Application du script

A partir du terminal, se placer dans le répertoire souhaité

### 1. Récupérer le repository GitHub et créer un environnement virtuel

Cloner le repository GitHub :
```bash
git clone https://github.com/Jennifer789C/Projet_10.git
```
Puis se placer dans le répertoire du projet :
```bash
cd Projet_10
```
*Pour ma part, je travaille sous Windows et avec l'IDE PyCharm, la création d'un environnement virtuel se fait via les paramètres de l'IDE*

Depuis un terminal sous Windows :
```bash
python -m venv env
env/Scripts/activate
```

Depuis un terminal sous Linux ou Mac :
```bash
python3 -m venv env
source env/bin/activate
```

### 2. Installer les packages du fichier requirements.txt

Dans l'environnement virtuel, télécharger l'ensemble des packages indiqués 
dans le fichier requirements.txt :
```bash
pip install -r requirements.txt
```

### 3. Ouvrir le site et le parcourir

Se placer dans le répertoire du projet Django :
```bash
cd SoftDesk
```
Lancer le script python :
```bash
python manage.py runserver
```
Se connecter à Postman afin de parcourir les différents endpoints.  
La documentation de cette API se trouve à l'adresse suivante :  
https://documenter.getpostman.com/view/23176759/2s8YzZQzbA

### 3. Détails de connexion des utilisateurs déjà inscrits

Quatre utilisateurs sont déjà inscrits et présents dans la base de données :  

    - un superuser (id : 1) : 
        * mail : admin@mail.fr  
        * mot de passe : mdpAdmin  
        * responsable du projet (id) : 1 
        * contributeur du projet (id) : 1
        * auteur du problème (id) : 4 (projet 1)
        * auteur du commentaire (id) : 1 du problème 1

    - un 1er utilisateur (id : 2) :  
        * mail : jennifer@mail.fr  
        * mot de passe : mdpjennifer  
        * responsable du projet (id) : 2, 3
        * contributeur du projet (id) : 2, 3
        * auteur du problème (id) : 5 (projet 2)
        * auteur du commentaire (id) : néant

    - un 2e utilisateur (id : 3) :  
        * mail : laura@mail.fr  
        * mot de passe : mdplaura 
        * responsable du projet (id) : néant
        * contributeur du projet (id) : néant
        * auteur du problème (id) : néant
        * auteur du commentaire (id) : néant 

    - un 3e utilisateur (id : 4) :  
        * mail : john@mail.fr  
        * mot de passe : mdpjohn
        * responsable du projet (id) : néant
        * contributeur du projet (id) : 1
        * auteur du problème (id) : 1 (projet 1)
        * auteur du commentaire (id) : néant