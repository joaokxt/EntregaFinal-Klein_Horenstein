from django.db import models
from datetime import date

# Create your models here.

class Actor(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.IntegerField()
    def __str__(self):
        return f"{self.nombre} {self.apellido} ({self.edad}) "

class Blog(models.Model):
    ESTRELLAS  = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    )

    GENEROS = (
        ('Acción', 'Acción'),
        ('Drama', 'Drama'),
        ('Terror', 'Terror'),
        ('Ciencia-ficción', 'Ciencia-ficción'),
        ('Comedia', 'Comedia'),
        ('Fantasia', 'Fantasia'),
    )
    titulo = models.CharField(max_length=50)
    subtitulo = models.CharField(max_length=50)
    anio = models.IntegerField()
    duracion = models.IntegerField()
    genero = models.CharField(max_length=30, choices=GENEROS)
    resenia = models.CharField(max_length=500)
    estrellas = models.CharField(max_length=2, choices=ESTRELLAS)
    autor = models.CharField(max_length=50)
    fecha = date.today()
    imagen = models.ImageField(upload_to='images/', null=True, blank=True)
    def __str__(self):
        return f"{self.titulo} ({self.anio}) || {self.estrellas}/5"


class Director(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.IntegerField()
    def __str__(self):
        return f"{self.nombre} {self.apellido} ({self.edad}) "
    







