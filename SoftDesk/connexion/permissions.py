from rest_framework.permissions import BasePermission
from .models import Contributeur


class EstContributeur(BasePermission):
    def has_permission(self, request, view):
        contributeurs = Contributeur.objects.filter(
            projet=view.kwargs["projects_pk"]
        )
        liste = []
        for contributeur in contributeurs:
            liste.append(contributeur.user)
        if request.user in liste:
            return True
        return False


class EstResponsable(BasePermission):
    def has_permission(self, request, view):
        responsable = Contributeur.objects.get(
            projet=view.kwargs["projects_pk"], role="Responsable"
        )
        if request.user == responsable.user:
            return True
        return False


class EstContributeurProjet(BasePermission):
    def has_permission(self, request, view):
        return
