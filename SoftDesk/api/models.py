from django.db import models
from django.conf import settings


class Projet(models.Model):
    class Type(models.TextChoices):
        Back_end = "Back-end"
        Front_end = "Front-end"
        Ios = "iOS"
        Android = "Android"

    titre = models.CharField(max_length=128)
    description = models.CharField(max_length=2048)
    type = models.CharField(choices=Type.choices, max_length=10)
    contributeurs = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                           through="connexion.Contributeur",
                                           related_name="contributions")
    accessible = models.BooleanField(default=False)


class Probleme(models.Model):
    class Priorite(models.TextChoices):
        Faible = "Faible"
        Moyenne = "Moyenne"
        Elevee = "Elevee"

    class Balise(models.TextChoices):
        Bug = "Bug"
        Amelioration = "Amelioration"
        Tache = "Tache"

    class Statut(models.TextChoices):
        A_faire = "À faire"
        En_cours = "En cours"
        Termine = "Terminé"

    titre = models.CharField(max_length=128)
    description = models.CharField(max_length=2048)
    balise = models.CharField(choices=Balise.choices, max_length=15)
    priorite = models.CharField(choices=Priorite.choices, max_length=10)
    statut = models.CharField(choices=Statut.choices, max_length=10)
    date = models.DateTimeField(auto_now_add=True)
    projet = models.ForeignKey(Projet, on_delete=models.CASCADE)
    auteur = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE,
                               related_name="auteur")
    assigne = models.ForeignKey(settings.AUTH_USER_MODEL,
                                on_delete=models.SET(auteur),
                                related_name="assigne")


class Commentaire(models.Model):
    description = models.CharField(max_length=2048)
    date = models.DateTimeField(auto_now_add=True)
    auteur = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE)
    probleme = models.ForeignKey(Probleme, on_delete=models.CASCADE)
