from rest_framework.serializers import ModelSerializer, ValidationError
from .models import Projet, Probleme, Commentaire


class ProjetListeSerializer(ModelSerializer):
    class Meta:
        model = Projet
        fields = ["id", "titre", "description", "type", "contributeurs"]

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


class ProblemeSerializer(ModelSerializer):
    class Meta:
        model = Probleme
        fields = ["id", "titre", "description", "balise", "priorite", "statut",
                  "date", "projet", "auteur", "assigne"]


class CommentaireSerializer(ModelSerializer):
    class Meta:
        model = Commentaire
        fields = ["id", "description", "date", "auteur", "probleme"]
