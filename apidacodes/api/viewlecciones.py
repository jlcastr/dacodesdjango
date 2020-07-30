from rest_framework import viewsets
from . import models
from . import serializers


# Create your views here.
class ApiLeccionesViewset(viewsets.ModelViewSet):
    queryset = models.Lecciones.objects.all()
    serializer_class = serializers.LeccionesSerializer
