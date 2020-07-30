"""apidacodes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .router import router
from . import view

#from .routerlecciones import router
#from rest_framework import routers





urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include(router.urls)),
    path('api/',view.apiinit, name='apiinit'),
    path('api/',view.actualizarcurso, name='actualizarcursos'),
    path('api/',view.actualizarusuario, name='actualizarusuarios'),
    path('api/',view.actualizarleccion, name='actualizarlecciones'),
    path('api/',view.actualizarpregunta, name='actualizarpreguntas'),
    
    path('api/',view.detallescurso, name='detallescursos'),
    

    
   # path('api/',include(router.urls))
]
