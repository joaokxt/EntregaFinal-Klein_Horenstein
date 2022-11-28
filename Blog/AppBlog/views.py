from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import *
from .forms import *
from datetime import date

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

def about_us(request):
    return render(request, "about_us.html")

def crear_blog(request):

    if request.method == "POST":
        formulario = BlogForm(request.POST)
        if formulario.is_valid():
            fomrulario_limpio = formulario.cleaned_data
            blog = Blog(titulo=fomrulario_limpio["titulo"],subtitulo=fomrulario_limpio["subtitulo"],anio=fomrulario_limpio["anio"],duracion=fomrulario_limpio["duracion"],genero=fomrulario_limpio["genero"],resenia=fomrulario_limpio["resenia"],estrellas=fomrulario_limpio["estrellas"],autor=fomrulario_limpio["autor"],fecha=date.today())
            blog.save()
            blogs = Blog.objects.all()
            return render(request, "base.html", {"blogs":blogs})
    
    else:
        formulario = BlogForm()
    
    return render(request, "crear_blog.html", {"formulario":formulario})

class SignupView(CreateView):
    form_class=SignUpForm
    success_url=reverse_lazy('inicio')
    template_name='signup.html'

class AdminLoginView(LoginView):
    template_name='login.html'

class AdminLogoutView(LogoutView):
    template_name='logout.html'




