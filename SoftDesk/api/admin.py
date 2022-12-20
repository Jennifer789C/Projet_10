from django.contrib import admin
from . import models


class ProjetAdmin(admin.ModelAdmin):
    list_display = ("id", "titre", "description")


admin.site.register(models.Projet, ProjetAdmin)


class ProblemeAdmin(admin.ModelAdmin):
    list_display = ("id", "titre", "statut", "projet", "auteur")


admin.site.register(models.Probleme, ProblemeAdmin)


class CommentaireAdmin(admin.ModelAdmin):
    list_display = ("id", "description", "probleme", "auteur")


admin.site.register(models.Commentaire, CommentaireAdmin)
