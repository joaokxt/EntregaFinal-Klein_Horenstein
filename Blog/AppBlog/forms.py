from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *
from datetime import date

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

#class BlogForm(forms.Form):
#    titulo = forms.CharField(label="Título del film",max_length=50)
#    anio = forms.DateField(label="Año de lanzamiento")
#    duracion = forms.IntegerField(label="Duración en minutos")
#    genero = forms.ChoiceField(label="Género",choices=Blog.GENEROS)
#    imagen = forms.ImageField(label="Portada")
#    subtitulo = forms.CharField(label="Título de reseña",max_length=50)
#    resenia = forms.CharField(label="Reseña", max_length=1000, widget=forms.Textarea())
#    estrellas = forms.ChoiceField(label="Estrellas",choices=Blog.ESTRELLAS)
#    autor = forms.CharField(label="Autor de reseña",max_length=50)
#    fecha = forms.DateField(label="Fecha de publicación")