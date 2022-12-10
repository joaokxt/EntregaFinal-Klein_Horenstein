from django.shortcuts import render
from django.contrib.auth import get_user
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from AppBlog.models import *
from .models import *
from .forms import *

def mostrar_usuario(request, blog_autor):
    user = User.objects.get(username=blog_autor)
    avatar = Avatar.objects.filter(user=user)
    if avatar==None:
        url=None
    else:
        url=avatar[0].imagen.url
    blogs = Blog.objects.filter(autor=blog_autor)
    return render(request, "mostrar_usuario.html", {"url":url, "usuario":user, "blogs":blogs})

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
            return render(request, 'index.html')
    else:
        formulario=AvatarForm()
    return render(request, 'agregar_avatar.html', {'formulario':formulario})


@login_required
def mi_perfil(request):
    avatar = Avatar.objects.filter(user=request.user.id)
    try:
        url=avatar[0].imagen.url
        sin_avatar=False
    except:
        url=None
        sin_avatar=True
    user = get_user(request)
    return render(request, "mi_perfil.html", {"url":url, "usuario":user, "sin_avatar":sin_avatar})

@login_required
def editar_perfil(request):
    usuario = request.user
    if request.method == "POST":
        formulario = UserEditForm(request.POST)
        if formulario.is_valid:
            informacion = formulario.cleaned_data
            usuario.email = informacion["email"]
            usuario.password1["password1"]
            usuario.password2["password2"]
            usuario.save()

            return render(request, "mostrar_usuario.html")
    
    else:
        formulario = UserEditForm(initial={"email":usuario.email})
    
    return render(request, "editar_usuario.html", {"formulario":formulario, "usuario":usuario})

class SignupView(CreateView):
    form_class=SignUpForm
    success_url=reverse_lazy('inicio')
    template_name='signup.html'

class AdminLoginView(LoginView):
    template_name='login.html'

class AdminLogoutView(LogoutView):
    template_name='index.html'