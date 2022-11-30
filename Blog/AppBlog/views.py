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


def index(request):
    blogs = Blog.objects.all()
    if blogs:
        blog = random.choice(blogs)
    else:
        blog = None
    return render(request, "index.html", {"blogs":blogs,"blog":blog})


def mostrar_blogs(request):
    blogs = Blog.objects.all()
    return render(request, "mostrar_blogs.html", {"blogs":blogs})


def mostrar_blog(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    return render(request, "mostrar_blog.html", {"blog":blog})


def eliminar_blog(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    blog.delete()
    blogs = Blog.objects.all()
    return render(request, "mostrar_blogs.html", {"blogs":blogs})


def crear_blog(request):
    if request.method == "POST":
        formulario = BlogForm(request.POST)
        if formulario.is_valid():
            info = formulario.cleaned_data
            blog = Blog(titulo=info["titulo"],subtitulo=info["subtitulo"],anio=info["anio"],duracion=info["duracion"],genero=info["genero"],resenia=info["resenia"],estrellas=info["estrellas"],autor=info["autor"],fecha=info["fecha"])
            blog.save()
            blogs = Blog.objects.all()
            return render(request, "mostrar_blogs.html", {"blogs":blogs})
    else:
        usuario=get_user(request)
        fecha=date.today()
        initial_data={
            'autor':usuario,
            'fecha':fecha,
        }
        formulario = BlogForm(initial=initial_data)
    return render(request, "crear_blog.html", {"formulario":formulario})


def editar_blog(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    if request.method == 'POST':
        formulario = BlogForm(request.POST)
        if formulario.is_valid():
            info = formulario.cleaned_data
            blog.titulo = info['titulo']
            blog.subtitulo = info['subtitulo']
            blog.anio = info['anio']
            blog.duracion = info['duracion']
            blog.genero = info['genero']
            blog.resenia = info['resenia']
            blog.estrellas = info['estrellas']
            blog.autor = info['autor']
            blog.fecha = info['fecha']
            blog.save()
            blogs=Blog.objects.all()
            return render(request, 'mostrar_blogs.html', {'blogs':blogs})
    else:
        usuario=get_user(request)
        fecha=date.today()
        initial_data={
            'autor':usuario,
            'fecha':fecha,
        }
        formulario = BlogForm(initial=initial_data)
    return render(request, 'editar_blog.html', {'formulario':formulario})

def buscar_blog(request):
    if request.GET.get("autor", False):
        autor=request.GET["autor"]
        blogs = Blog.objects.filter(autor_icontains=autor)
        return render(request, "buscar_blog.html", {"blogs":blogs})
    else:
        mensaje="Ingresa algo"
    return render(request, "buscar_blog.html", {"mensaje":mensaje})


def mostrar_actor(request):
    actores = Actor.objects.all()
    return render(request, "mostrar_actor.html", {"actores":actores})


def agregar_actor(request):
    pass


def mostrar_generos(request):
    return render(request, "generos.html")


def accion(request):
    lista_accion = []
    blogs = list(Blog.objects.all())
    for blog in blogs:
        if blog.genero == "Acción":
            lista_accion.append(blog)
    return render(request, "accion.html", {"lista_accion":lista_accion})


def drama(request):
    lista_drama = []
    blogs = list(Blog.objects.all())
    for blog in blogs:
        if blog.genero == "Drama":
            lista_drama.append(blog)
    return render(request, "drama.html", {"lista_drama":lista_drama})


def terror(request):
    lista_terror = []
    blogs = list(Blog.objects.all())
    for blog in blogs:
        if blog.genero == "Terror":
            lista_terror.append(blog)
    return render(request, "terror.html", {"lista_terror":lista_terror})


def ciencia_ficcion(request):
    lista_ciencia_ficcion = []
    blogs = list(Blog.objects.all())
    for blog in blogs:
        if blog.genero == "Ciencia-Ficción":
            lista_ciencia_ficcion.append(blog)
    return render(request, "ciencia_ficcion.html", {"lista_ciencia_ficcion":lista_ciencia_ficcion})


def comedia(request):
    lista_comedia = []
    blogs = list(Blog.objects.all())
    for blog in blogs:
        if blog.genero == "Comedia":
            lista_comedia.append(blog)
    return render(request, "comedia.html", {"lista_comedia":lista_comedia})


def fantasia(request):
    lista_fantasia = []
    blogs = list(Blog.objects.all())
    for blog in blogs:
        if blog.genero == "Fantasia":
            lista_fantasia.append(blog)
    return render(request, "fantasia.html", {"lista_fantasia":lista_fantasia})


def about_us(request):
    return render(request, "about_us.html")

class SignupView(CreateView):
    form_class=SignUpForm
    success_url=reverse_lazy('inicio')
    template_name='signup.html'

class AdminLoginView(LoginView):
    template_name='login.html'

class AdminLogoutView(LogoutView):
    template_name='logout.html'




