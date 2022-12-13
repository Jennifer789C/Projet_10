from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from .serializers import ProjetListeSerializer, ProjetDetailSerializer, \
    ContributeurListeSerializer, ContributeurAjoutSerializer
from .models import Projet
from connexion.models import Contributeur
from connexion.permissions import EstContributeur

User = get_user_model()


class ProjetViewset(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = ProjetListeSerializer
    detail_serializer_class = ProjetDetailSerializer

    def get_queryset(self):
        contributeurs = Contributeur.objects.all()
        for contributeur in contributeurs:
            if self.request.user == contributeur.user:
                contributeur.projet.accessible = True
            else:
                contributeur.projet.accessible = False
            contributeur.projet.save()
        return Projet.objects.filter(accessible=True)

    def get_serializer_class(self):
        if self.action == "list" or self.action == "create":
            return super().get_serializer_class()
        return self.detail_serializer_class

    def perform_create(self, serializer):
        utilisateur = User.objects.get(id=self.request.user.id)
        projet = serializer.save()
        projet.contributeurs.add(utilisateur,
                                 through_defaults={"role": "Responsable"})
        projet.save()


class UserViewset(ModelViewSet):
    permission_classes = [IsAuthenticated, EstContributeur]

    def get_queryset(self):
        return Contributeur.objects.filter(projet=self.kwargs["projects_pk"])

    def get_serializer_class(self):
        if self.action == "list":
            return ContributeurListeSerializer
        elif self.action == "create":
            return ContributeurAjoutSerializer

    def perform_create(self, serializer):
        projet = Projet.objects.get(id=self.kwargs["projects_pk"])
        serializer.save(projet=projet, role="Contributeur")
