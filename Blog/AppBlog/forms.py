from django import forms
from django.forms import ModelForm
from .models import *

class BlogForm(ModelForm):
    class Meta:
        model=Blog
        fields='__all__'
        labels={
            'titulo':"Título del film",
            'anio':"Año de lanzamiento",
            'duracion':"Duración en minutos",
            'genero':"Género",
            'imagen':"Portada",
            'subtitulo':"Título de reseña",
            'resenia':"Reseña",
            'estrellas':"Estrellas",
            'autor':"Autor de reseña",
            'fecha':"Fecha de publicación",
        }
        widgets={
            'resenia':forms.Textarea(),
            'autor':forms.TextInput(attrs={'readonly':'readonly'}),
            'fecha':forms.TextInput(attrs={'readonly':'readonly'}),
        }
