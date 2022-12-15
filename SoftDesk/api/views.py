from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from .serializers import ProjetListeSerializer, ProjetDetailSerializer, \
    ContributeurListeSerializer, ContributeurAjoutSerializer, \
    ProblemeListeSerializer, ProblemeDetailSerializer, ProblemeModifSerializer, \
    CommentaireListeSerializer, CommentaireDetailSerializer
from .models import Projet, Probleme, Commentaire
from connexion.models import Contributeur
from connexion.permissions import EstContributeur, EstResponsable, \
    EstResponsableProjet, EstAuteurProbleme, EstAuteurComment

User = get_user_model()


class ProjetViewset(ModelViewSet):
    def get_queryset(self):
        contributeurs = Contributeur.objects.filter(user=self.request.user)
        non_contributeurs = Contributeur.objects.all().exclude(
            user=self.request.user
        )
        for contributeur in non_contributeurs:
            contributeur.projet.accessible = False
            contributeur.projet.save()
        for contributeur in contributeurs:
            contributeur.projet.accessible = True
            contributeur.projet.save()
        return Projet.objects.filter(accessible=True)

    def get_serializer_class(self):
        if self.action == "list" or self.action == "create":
            return ProjetListeSerializer
        return ProjetDetailSerializer

    def get_permissions(self):
        if self.action == "list" or \
                self.action == "create" or \
                self.action == "retrieve":
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAuthenticated, EstResponsableProjet]
        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        utilisateur = User.objects.get(id=self.request.user.id)
        projet = serializer.save()
        projet.contributeurs.add(utilisateur,
                                 through_defaults={"role": "Responsable"})
        projet.save()


class UserViewset(ModelViewSet):
    def get_queryset(self):
        return Contributeur.objects.filter(projet=self.kwargs["projects_pk"])

    def get_serializer_class(self):
        if self.action == "list":
            return ContributeurListeSerializer
        elif self.action == "create":
            return ContributeurAjoutSerializer

    def get_permissions(self):
        if self.action == "list":
            permission_classes = [IsAuthenticated, EstContributeur]
        else:
            permission_classes = [IsAuthenticated, EstResponsable]
        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        projet = Projet.objects.get(id=self.kwargs["projects_pk"])
        serializer.save(projet=projet, role="Contributeur")


class ProblemeViewset(ModelViewSet):
    def get_queryset(self):
        return Probleme.objects.filter(projet=self.kwargs["projects_pk"])

    def get_serializer_class(self):
        if self.action == "list" or self.action == "create":
            return ProblemeListeSerializer
        elif self.action == "update":
            return ProblemeModifSerializer
        else:
            return ProblemeDetailSerializer

    def get_permissions(self):
        if self.action == "list" or \
                self.action == "create" or \
                self.action == "retrieve":
            permission_classes = [IsAuthenticated, EstContributeur]
        else:
            permission_classes = [IsAuthenticated, EstAuteurProbleme]
        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        projet = Projet.objects.get(id=self.kwargs["projects_pk"])
        auteur = self.request.user
        serializer.save(projet=projet, auteur=auteur, assigne=auteur)

    def perform_update(self, serializer):
        projet = Projet.objects.get(id=self.kwargs["projects_pk"])
        auteur = self.request.user
        serializer.save(projet=projet, auteur=auteur)


class CommentaireViewset(ModelViewSet):
    def get_queryset(self):
        return Commentaire.objects.filter(probleme=self.kwargs["issues_pk"])

    def get_serializer_class(self):
        if self.action == "list" or \
                self.action == "create" or \
                self.action == "update":
            return CommentaireListeSerializer
        else:
            return CommentaireDetailSerializer

    def get_permissions(self):
        if self.action == "list" or \
                self.action == "create" or \
                self.action == "retrieve":
            permission_classes = [IsAuthenticated, EstContributeur]
        else:
            permission_classes = [IsAuthenticated, EstAuteurComment]
        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        probleme = Probleme.objects.get(id=self.kwargs["issues_pk"])
        auteur = self.request.user
        serializer.save(probleme=probleme, auteur=auteur)

    def perform_update(self, serializer):
        probleme = Probleme.objects.get(id=self.kwargs["issues_pk"])
        auteur = self.request.user
        serializer.save(probleme=probleme, auteur=auteur)
