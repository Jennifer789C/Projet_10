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
