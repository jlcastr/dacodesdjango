from rest_framework import serializers
from .models import UsuarioRoll,Respuestas,Preguntas,Lecciones,Curso


class UsuariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsuarioRoll
        fields = '__all__'



class PreguntasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Preguntas
        fields = '__all__'

class LeccionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lecciones
        fields = '__all__'

class CursosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'



  