from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.views import LoginView, LogoutView
from .models import *

# Create your views here.
def index(request):
    return render(request, 'index.html')
    
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

class AdminLoginView(LoginView):
    template_name='login.html'

class AdminLogoutView(LogoutView):
    template_name='logout.html'




