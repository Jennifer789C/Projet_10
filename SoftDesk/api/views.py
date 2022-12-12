from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ModelViewSet
from .serializers import ProjetSerializer
from .models import Projet

User = get_user_model()


class ProjetViewset(ModelViewSet):
    serializer_class = ProjetSerializer

    def get_queryset(self):
        return Projet.objects.all()

    def perform_create(self, serializer):
        utilisateur = User.objects.get(id=self.request.user.id)
        projet = serializer.save()
        projet.contributeurs.add(utilisateur,
                                 through_defaults={"role": "Responsable"})
        projet.save()
