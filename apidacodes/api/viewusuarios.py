from rest_framework import viewsets
from . import models
from . import serializers

class ApiUsuarios(viewsets.ModelViewSet):
    queryset = models.UsuarioRoll.objects.all()
    serializer_class = serializers.UsuariosSerializer

    

