from rest_framework.serializers import ModelSerializer, CharField, \
    ValidationError
from django.contrib.auth import get_user_model

User = get_user_model()


class InscriptionSerializer(ModelSerializer):
    password2 = CharField(label="Confirmation du mot de passe",
                          write_only=True)

    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "password", "password2"]

        extra_kwargs = {"password": {"write_only": True}}

    def validate_first_name(self, value):
        if value == "":
            raise ValidationError("Ce champ ne peut être vide.")
        return value

    def validate_last_name(self, value):
        if value == "":
            raise ValidationError("Ce champ ne peut être vide.")
        return value

    def validate(self, data):
        if data["password"] != data["password2"]:
            raise ValidationError("les mots de passe doivent correspondre.")
        return data

    def create(self, validated_data):
        first_name = validated_data["first_name"]
        last_name = validated_data["last_name"]
        email = validated_data["email"]
        password = validated_data["password"]
        utilisateur = User(
            first_name=first_name,
            last_name=last_name,
            email=email
        )
        utilisateur.set_password(password)
        utilisateur.save()
        return validated_data
