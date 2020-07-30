# dacodesdjango
Api django con tematica e-learning. Permite tener acceso a un CRUD básico de  usuarios, cursos, lecciones y preguntas.  

## Herramientas usadas

**Postgres:** Una solución útil y fácil de integrar con el lenguaje Python, alta compatibilidad para trabajar con frameworks dedicados al desarrollo web, como lo son Django y Flask.

**Django REST:** construir apis de manera sencilla, permite minimizar el código e incrementar el desarrollo ágil. 



## Instalación de librerias

- activar entorno virtual con el que se va a trabajar

Instalar el archivo requirements.txt con el comando:

- *pip install -r requirements.txt*

## Instalar base de datos 

**Opción 1**

- Ir al pgadmin

- Crear base de datos y asignarle un nombre

- Click derecho en la base de datos y seleccionar "Restore"

- Buscamos el archivo "dbpost"

- Seleccionamos el rol "postgres"

- Presionamos "Restore"


**Opcion 2**

- Crear una base de datos de nombre "cursoscodes"

- Crear los campos mediente django


## Configuración de Django

Ejecutar los siguientes comandos en la terminal, con el entorno de python activado.

- python manage.py makemigrations api

- python manage.py migrate

- python mange.py runserver


## Direcciones del sistema

La api cuenta con las funciones de insertar, visualizar, editar y eliminar.

Direcciones de las funciones.

-http://127.0.0.1:8000/api/: Direcciones

-http://127.0.0.1:8000/api/usuarios/: Agregar usuarios

-http://127.0.0.1:8000/api/cursos/: Agregar cursos

-http://127.0.0.1:8000/api/lecciones/: Agregar lecciones

-http://127.0.0.1:8000/api/preguntas/: Agregar preguntas

Actualizar y Eliminar.

Remplazar "Idbuscado" por un número para visualizar el registro con ese id y de esa manera actualizar o eliminar el registro.

-http://127.0.0.1:8000/api/actualizarcursos/ **Idbuscado** Cursos

-http://127.0.0.1:8000/api/actualizarusuarios/ **Idbuscado** Usuarios

-http://127.0.0.1:8000/api/actualizarlecciones/ **Idbuscado** Lecciones

-http://127.0.0.1:8000/api/actualizarpreguntas/ **Idbuscado** Preguntas
