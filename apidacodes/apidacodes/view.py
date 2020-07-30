from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.serializers import CursosSerializer

@api_view(['GET'])
def apiinit(request):
    api_urls = {
        'Insertar/Detalles Usuario':'/usuarios/',
        'Insertar/Detalles Curso':'/cursos/',
        'Insertar/Detalles Lecciones':'/lecciones/',
        'Insertar/Detalles preguntas':'/preguntas/',
        '#Instrucciones para actualizar/eliminar':'/actualizarcursos/Idbuscado/',
        'Actualizar/EliminarCurso':'/actualizarcursos/',
        'Actualizar/EliminarUsuario':'/actualizarusuarios/',
        'Actualizar/EliminarLecciones':'/actualizarlecciones/',
        'Actualizar/EliminarPreguntas':'/actualizarpreguntas/',


    }
    return Response(api_urls)

@api_view(['GET'])
def detallescurso(request):
    detalle = Task.objects.all()
    serializer = CursosSerializer(detalle, many=True)
    return Response(serializer.data)

#actualización/eliminar de registros 
@api_view(['POST'])
def actualizarcurso(request, pk):
    actualizacioncursos = Task.objects.get(id=pk)
    serializer = CursosSerializer(instance=actualizacioncursos, data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def actualizarusuario(request, pk):
    actualizacionusuarios = Task.objects.get(id=pk)
    serializer = CursosSerializer(instance=actualizacionusuarios, data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def actualizarleccion(request, pk):
    actualizalecciones = Task.objects.get(id=pk)
    serializer = CursosSerializer(instance=actualizalecciones, data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def actualizarpregunta(request, pk):
    actualizapreguntas = Task.objects.get(id=pk)
    serializer = CursosSerializer(instance=actualizapreguntas, data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

