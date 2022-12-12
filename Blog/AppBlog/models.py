from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

# Create your models here.

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
    titulo = models.CharField(max_length=80)
    subtitulo = models.CharField(max_length=50)
    anio = models.DateField()
    duracion = models.IntegerField()
    genero = models.CharField(max_length=30, choices=GENEROS)
    resenia = RichTextField(config_name='awesome_ckeditor')
    estrellas = models.CharField(max_length=2, choices=ESTRELLAS)
    autor = models.CharField(max_length=50)
    fecha = models.DateTimeField()
    imagen = models.ImageField(upload_to='imagenes/', null=True, blank=True)
    def __str__(self):
        return f"{self.titulo} ({self.anio}) || {self.estrellas}/5 || Por {self.autor}"

class Comentario(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    texto = models.CharField(max_length=150)
    autor = models.CharField(max_length=50)
    fecha = models.DateTimeField()