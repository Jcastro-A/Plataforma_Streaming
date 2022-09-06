from django.contrib import admin
from streapp.models import Peliculas, Series, Documentales

# Registros que nos traemos de la base de datos.

admin.site.register(Peliculas)
admin.site.register(Series)
admin.site.register(Documentales)
