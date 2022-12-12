from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from .serializers import ProjetListeSerializer, ProjetDetailSerializer
from .models import Projet

User = get_user_model()


class ProjetViewset(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = ProjetListeSerializer
    detail_serializer_class = ProjetDetailSerializer

    def get_queryset(self):
        return Projet.objects.all()

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
