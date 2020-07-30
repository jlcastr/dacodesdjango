from api.viewsets import ApiViewset
from rest_framework import routers
from api.views import ApiLeccionesViewset

router = routers.DefaultRouter()

router.register('lecciones',ApiLeccionesViewset)
