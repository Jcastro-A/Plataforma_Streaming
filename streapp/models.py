from django.db import models

# Creacion de modelos para la base de datos.

class Peliculas(models.Model):
    nombre = models.CharField(max_length=128)
    genero = models.CharField(max_length=128)
    fecha = models.DateField() 
    aptoPara = models.IntegerField()
    def __str__(self):
        return f"{self.nombre} - {self.genero}"

class Series(models.Model):
    nombre = models.CharField(max_length=128)
    genero = models.CharField(max_length=128)
    fecha = models.DateField()
    aptoPara = models.IntegerField()
    def __str__(self):
        return f"{self.nombre} - {self.genero}"


class Documentales(models.Model):
    nombre = models.CharField(max_length=128)
    genero = models.CharField(max_length=128)
    fecha = models.DateField()
    aptoPara = models.IntegerField()
    def __str__(self):
        return f"{self.nombre} - {self.genero}"