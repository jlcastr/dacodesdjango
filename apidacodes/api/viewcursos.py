from rest_framework import viewsets
from . import models
from . import serializers


# Create your views here.
class ApiCursosViewset(viewsets.ModelViewSet):
    queryset = models.Curso.objects.all()
    serializer_class = serializers.CursosSerializer
