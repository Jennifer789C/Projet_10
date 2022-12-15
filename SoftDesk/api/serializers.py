from rest_framework.serializers import ModelSerializer, ValidationError
from .models import Projet, Probleme, Commentaire
from connexion.models import Contributeur


class ProjetListeSerializer(ModelSerializer):
    class Meta:
        model = Projet
        fields = ["id", "titre", "description", "type"]

    def validate_titre(self, value):
        if value == "":
            raise ValidationError("Ce champ ne peut être vide.")
        return value

    def validate_description(self, value):
        if value == "":
            raise ValidationError("Ce champ ne peut être vide.")
        return value


class ProjetDetailSerializer(ModelSerializer):
    class Meta:
        model = Projet
        fields = ["id", "titre", "description", "type", "contributeurs"]


class ContributeurListeSerializer(ModelSerializer):
    parent_lookup_kwargs = {"projects_pk": "projects__pk"}

    class Meta:
        model = Contributeur
        fields = ["id", "user", "role"]


class ContributeurAjoutSerializer(ModelSerializer):
    parent_lookup_kwargs = {"projects_pk": "projects__pk"}

    class Meta:
        model = Contributeur
        fields = ["user"]


class ProblemeListeSerializer(ModelSerializer):
    parent_lookup_kwargs = {"projects_pk": "projects__pk"}

    class Meta:
        model = Probleme
        fields = ["id", "titre", "description", "balise", "priorite", "statut"]

    def validate_titre(self, value):
        if value == "":
            raise ValidationError("Ce champ ne peut être vide.")
        return value

    def validate_description(self, value):
        if value == "":
            raise ValidationError("Ce champ ne peut être vide.")
        return value


class ProblemeModifSerializer(ModelSerializer):
    parent_lookup_kwargs = {"projects_pk": "projects__pk"}

    class Meta:
        model = Probleme
        fields = ["id", "titre", "description", "balise", "priorite", "statut",
                  "assigne"]


class ProblemeDetailSerializer(ModelSerializer):
    parent_lookup_kwargs = {"projects_pk": "projects__pk"}

    class Meta:
        model = Probleme
        fields = ["id", "titre", "description", "balise", "priorite", "statut",
                  "date", "projet", "auteur", "assigne"]


class CommentaireSerializer(ModelSerializer):
    class Meta:
        model = Commentaire
        fields = ["id", "description", "date", "auteur", "probleme"]
