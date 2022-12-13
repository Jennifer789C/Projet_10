from rest_framework.permissions import BasePermission
from .models import Contributeur


class EstContributeur(BasePermission):
    def has_permission(self, request, view):
        contributeurs = Contributeur.objects.filter(projet=view.kwargs["projects_pk"])
        for contributeur in contributeurs:
            if request.user == contributeur.user:
                return True
            return False
