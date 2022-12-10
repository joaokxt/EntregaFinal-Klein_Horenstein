from django.shortcuts import render
from django.contrib.auth import get_user
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from .models import *
from .forms import *
from datetime import date
from django.urls import reverse_lazy
import random


def index(request):
    blogs = Blog.objects.all()
    if blogs:
        blog = random.choice(blogs)
    else:
        blog = None
    return render(request, "index.html", {"blogs":blogs,"blog":blog})


def mostrar_blogs(request, modo):
    blogs = Blog.objects.all()
    ver=False
    editar=False
    eliminar=False
    if modo == 'ver':
        ver=True
    elif modo == 'eliminar':
        eliminar=True
    elif modo == 'editar':
        editar=True
    return render(request, "mostrar_blogs.html", {"blogs":blogs, "ver":ver, "editar":editar, "eliminar":eliminar})


def mostrar_blog(request, blog_id):
    blog1 = Blog.objects.get(id=blog_id)
    if request.method == "POST":
        formulario = ComentarioForm(request.POST)
        if formulario.is_valid():
            info = formulario.cleaned_data
            comentario = Comentario(blog=blog1, texto=info["texto"], autor=info["autor"], fecha=info["fecha"])
            comentario.save()
            comentarios = Comentario.objects.filter(blog=blog1)
            return render(request, "mostrar_blog.html", {"blog":blog1, "comentarios":comentarios, "puede_comentar":False})
    else:
        comentarios = Comentario.objects.filter(blog=blog1)
        usuario=get_user(request)
        fecha=date.today()
        initial_data={
            'autor':usuario,
            'fecha':fecha,
        }
        formulario = ComentarioForm(initial=initial_data)
    return render(request, "mostrar_blog.html", {"blog":blog1, "url":blog1.imagen, "formulario":formulario, "comentarios":comentarios, "puede_comentar":True})


@login_required
def eliminar_blog(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    blog.delete()
    blogs = Blog.objects.all()
    return render(request, "mostrar_blogs.html", {"blogs":blogs})


@login_required
def crear_blog(request):
    if request.method == "POST":
        formulario = BlogForm(request.POST, request.FILES)
        if formulario.is_valid():
            info = formulario.cleaned_data
            blog = Blog(titulo=info["titulo"],subtitulo=info["subtitulo"],anio=info["anio"],duracion=info["duracion"],genero=info["genero"],resenia=info["resenia"],estrellas=info["estrellas"],autor=info["autor"],fecha=info["fecha"], imagen=info["imagen"])
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


@login_required
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
            blog.imagen = info['imagen']
            blog.save()
            blogs=Blog.objects.all()
            return render(request, 'mostrar_blogs.html', {'blogs':blogs})
    else:
        usuario=blog.autor
        fecha=blog.fecha
        initial_data={
            'autor':usuario,
            'fecha':fecha,
        }
        formulario = BlogForm(initial=initial_data)
    return render(request, 'editar_blog.html', {'formulario':formulario})


def buscar_blog(request):
    if request.GET.get("autor", False):
        autor=request.GET["autor"]
        blogs = Blog.objects.filter(autor__icontains=autor)
        return render(request, "buscar_blog.html", {"blogs":blogs})
    else:
        mensaje="Ingresa algo"
    return render(request, "buscar_blog.html", {"mensaje":mensaje})


def mostrar_generos(request):
    return render(request, "generos.html")


def genero(request, genero_nombre):
    blogs=list(Blog.objects.filter(genero=genero_nombre))
    return render(request, "genero_nombre.html", {"lista":blogs,"nombre":genero_nombre})


def about_us(request):
    return render(request, "about_us.html")