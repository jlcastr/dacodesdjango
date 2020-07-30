from rest_framework import viewsets
from . import models
from . import serializers

class ApiPreguntas(viewsets.ModelViewSet):
    queryset = models.Preguntas.objects.all()
    serializer_class = serializers.PreguntasSerializer

    



