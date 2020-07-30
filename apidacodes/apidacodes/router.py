from api.viewpreguntas import ApiPreguntas
from rest_framework import routers
from api.viewlecciones import ApiLeccionesViewset
from api.viewusuarios import ApiUsuarios
from api.viewcursos import ApiCursosViewset

#Rutas de las api´s
router = routers.SimpleRouter()
router.register('preguntas',ApiPreguntas)
router.register('lecciones',ApiLeccionesViewset)
router.register('usuarios',ApiUsuarios)
router.register('cursos', ApiCursosViewset)




#actualizar
router.register('actualizarcursos', ApiCursosViewset)
router.register('actualizarusuarios', ApiUsuarios)
router.register('actualizarlecciones', ApiLeccionesViewset)
router.register('actualizarpreguntas', ApiPreguntas)


