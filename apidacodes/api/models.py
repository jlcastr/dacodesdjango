from django.db import models

# Create your models here.

class UsuarioRoll(models.Model):
    idAlumno = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=150)
    #Rol --> Alumno, Profesor, Admi
    rol = models.CharField(max_length=30)

class Respuestas(models.Model):
    respuesta = models.CharField(max_length=300)
    RespuestaCorrecta = models.BooleanField(default=False)

    
class Preguntas(models.Model):
    idPregunta = models.AutoField(primary_key=True)
    pregunta = models.CharField(max_length=300)
    puntos = models.IntegerField(default=0)
    respuesta = {
        "Solo_una","solo una",
        "mas_de_una","Más de una es correcta",
        "correctas","Más de una correcta y todas deben ser respondidas",
    }

class Lecciones(models.Model):
    idLeccion = models.AutoField(primary_key=True)
    NombreLeccion = models.CharField(max_length=50)
   # preguntas = models.ForeignKey(to=Preguntas, on_delete=models.CASCADE)


class Curso(models.Model):
    idCurso = models.AutoField(primary_key=True)
    NombreCurso = models.CharField(max_length=100)
    Descripcion = models.CharField(max_length=150)
    lecciones = models.ForeignKey(to=Lecciones, on_delete=models.CASCADE)
