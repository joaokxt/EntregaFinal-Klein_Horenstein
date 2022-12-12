from django.shortcuts import render
from django.contrib.auth import get_user
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from AppBlog.models import *
from .models import *
from .forms import *

def mostrar_usuario(request, blog_autor):
    usuario = User.objects.get(username=blog_autor)
    avatar = Avatar.objects.filter(user=usuario)
    if avatar==None:
        url=None
    else:
        url=avatar[0].imagen.url
    bio = Bio.objects.filter(user=usuario)
    try:
        desc = bio[0].descripcion
        pag = bio[0].link
    except:
        desc = "El usuario todavía no dejó su descripción."
        pag = "Indisponible"
    blogs = Blog.objects.filter(autor=blog_autor)
    return render(request, "mostrar_usuario.html", {"url":url, "usuario":usuario, "blogs":blogs, "desc":desc, "pag":pag})


@login_required
def agregar_avatar(request):
    if request.method == 'POST':
        formulario = AvatarForm(request.POST, request.FILES)
        if formulario.is_valid():
            usuario=User.objects.get(username=request.user)
            info = formulario.cleaned_data
            try:
                avatar_viejo = Avatar.objects.get(user=usuario)
                avatar_viejo.delete()
            except:
                pass
            avatar=Avatar(user=usuario, imagen=info['imagen'])
            avatar.save()
            avatar = Avatar.objects.filter(user=request.user.id)
            img=avatar[0].imagen.url
            bio = Bio.objects.filter(user=request.user.id)
            try:
                desc = bio[0].descripcion
                pag = bio[0].link
            except:
                desc = "Indisponible"
                pag = "Indisponible"
            user = get_user(request)
            return render(request, 'mi_perfil.html', {"img":img, "usuario":user, "sin_avatar":False, "desc":desc, "pag":pag})
    else:
        formulario=AvatarForm()
    return render(request, 'agregar_avatar.html', {'formulario':formulario})


@login_required
def editar_bio(request):
    if request.method == 'POST':
        formulario = BioEditForm(request.POST)
        if formulario.is_valid():
            usuario=User.objects.get(username=request.user)
            info = formulario.cleaned_data
            try:
                bio_vieja = Bio.objects.get(user=usuario)
                bio_vieja.delete()
            except:
                pass
            bio=Bio(user=usuario, link=info['link'], descripcion=info['descripcion'])
            bio.save()
            avatar = Avatar.objects.filter(user=request.user.id)
            try:
                img=avatar[0].imagen.url
                sin_avatar=False
            except:
                img=None
                sin_avatar=True
            bio = Bio.objects.filter(user=request.user.id)
            desc = bio[0].descripcion
            link = bio[0].link
            user = get_user(request)
            return render(request, 'mi_perfil.html', {"img":img, "usuario":user, "sin_avatar":sin_avatar, "desc":desc, "link":link})
    else:
        formulario=BioEditForm()
        usuario=User.objects.get(username=request.user)
    return render(request, 'editar_bio.html', {'formulario':formulario, 'usuario':usuario})  


@login_required
def mi_perfil(request):
    user = get_user(request)
    avatar = Avatar.objects.filter(user=request.user)
    try:
        img=avatar[0].imagen.url
        sin_avatar=False
    except:
        img=None
        sin_avatar=True
    bio = Bio.objects.filter(user=request.user)
    try:
        desc = bio[0].descripcion
        pag = bio[0].link
    except:
        desc = "Indisponible"
        pag = "Indisponible"
    contexto = {
        "img":img,
        "usuario":user, 
        "sin_avatar":sin_avatar,
        "desc":desc,
        "pag":pag
        }
    return render(request, "mi_perfil.html", contexto)


@login_required
def editar_perfil(request):
    usuario = User.objects.get(id=request.user.id)
    if request.method == "POST":
        formulario = UserEditForm(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            usuario.email = informacion["email"]
            usuario.password1 = informacion["password1"]
            usuario.password2 = informacion["password2"]
            usuario.first_name = informacion["first_name"]
            usuario.last_name = informacion["last_name"]
            usuario.save()
        return render(request, "index.html")
    else:
        formulario = UserEditForm(initial={"email":usuario.email})
    return render(request, "editar_usuario.html", {"formulario":formulario, "usuario":usuario.username})


class SignupView(CreateView):
    form_class=SignUpForm
    success_url=reverse_lazy('login')
    template_name='signup.html'

class AdminLoginView(LoginView):
    template_name='login.html'

class AdminLogoutView(LogoutView):
    template_name='index.html'