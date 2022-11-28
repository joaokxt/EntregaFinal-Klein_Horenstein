from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *
from datetime import date

class SignUpForm(UserCreationForm):
    class Meta:
        model=User
        fields=[
            'username',
            'email',
            'password1',
            'password2',
        ]

class BlogForm(forms.Form):
    titulo = forms.CharField(max_length=50)
    subtitulo = forms.CharField(max_length=50)
    anio = forms.IntegerField()
    duracion = forms.IntegerField()
    genero = forms.CharField(max_length=30, choices=Blog.GENEROS)
    resenia = forms.CharField(max_length=500)
    estrellas = forms.CharField(choices=Blog.ESTRELLAS)
    autor = forms.CharField(max_length=50)
    fecha = date.today()
    imagen = forms.ImageField(upload_to='images/', null=True, blank=True)