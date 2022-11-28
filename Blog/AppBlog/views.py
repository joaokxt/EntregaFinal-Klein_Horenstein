from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import get_user
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import *
from .forms import *
from datetime import date
import random


# Create your views here.
def index(request):
    blogs = list(Blog.objects.all())
    random_blog = random.choice(blogs)
    return render(request, "index.html", {"blog":random_blog})
    
def mostrar_actor(request):
    actores = Actor.objects.all()
    return render(request, "mostrar_actor.html", {"actores":actores})

def agregar_actor(request):
    pass

def mostrar_generos(request):
    return render(request, "generos.html")

def accion(request):
    pass

def drama(request):
    pass

def terror(request):
    pass

def ciencia_ficcion(request):
    pass

def comedia(request):
    pass

def fantasia(request):
    pass

def about_us(request):
    return render(request, "about_us.html")

def crear_blog(request):
    if request.method == "POST":
        formulario = BlogForm(request.POST)
        if formulario.is_valid():
            info = formulario.cleaned_data
            blog = Blog(titulo=info["titulo"],subtitulo=info["subtitulo"],anio=info["anio"],duracion=info["duracion"],genero=info["genero"],resenia=info["resenia"],estrellas=info["estrellas"],autor=info["autor"],fecha=info["fecha"])
            blog.save()
            blogs = list(Blog.objects.all())
            random_blog = random.choice(blogs)
            return render(request, "index.html", {"blog":random_blog})
    else:
        usuario=get_user(request)
        fecha=date.today()
        initial_data={
            'autor':usuario,
            'fecha':fecha,
        }
        formulario = BlogForm(initial=initial_data)
    return render(request, "crear_blog.html", {"formulario":formulario})

class SignupView(CreateView):
    form_class=SignUpForm
    success_url=reverse_lazy('inicio')
    template_name='signup.html'

class AdminLoginView(LoginView):
    template_name='login.html'

class AdminLogoutView(LogoutView):
    template_name='logout.html'




