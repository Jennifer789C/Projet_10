from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from api.models import Projet


class User(AbstractUser):
    email = models.EmailField(unique=True)
    username = None
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []


class Contributeur(models.Model):
    class Role(models.TextChoices):
        Responsable = "Responsable"
        Contributeur = "Contributeur"
        Auteur = "Auteur"

    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE,
                             related_name="projets")
    projet = models.ForeignKey(Projet, on_delete=models.CASCADE,
                               related_name="utilisateurs")
    role = models.CharField(choices=Role.choices, max_length=15)

    class Meta:
        unique_together = ("user", "projet")
