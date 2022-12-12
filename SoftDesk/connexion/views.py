from rest_framework.generics import CreateAPIView
from django.contrib.auth import get_user_model
from .serializers import InscriptionSerializer

User = get_user_model()


class InscriptionAPIView(CreateAPIView):
    serializer_class = InscriptionSerializer
    queryset = User.objects.all()
