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


class ContributeurSerializer(ModelSerializer):
    parent_lookup_kwargs = {"projects_pk": "projects__pk"}
    projet = ProjetListeSerializer()

    class Meta:
        model = Contributeur
        fields = ["projet", "user", "role"]
        extra_kwargs = {"projet": {"read_only": True}}


class ProblemeSerializer(ModelSerializer):
    class Meta:
        model = Probleme
        fields = ["id", "titre", "description", "balise", "priorite", "statut",
                  "date", "projet", "auteur", "assigne"]


class CommentaireSerializer(ModelSerializer):
    class Meta:
        model = Commentaire
        fields = ["id", "description", "date", "auteur", "probleme"]
