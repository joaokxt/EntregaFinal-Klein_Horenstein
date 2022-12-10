from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *

class SignUpForm(UserCreationForm):
    email = forms.EmailField()
    username = forms.CharField(label='Nombre de usuario')
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir contraseña', widget=forms.PasswordInput)
    first_name = forms.CharField(label='Nombre')
    last_name = forms.CharField(label='Apellido')
    class Meta:
        model=User
        fields=[
            'username',
            'email',
            'password1',
            'password2',
            'first_name',
            'last_name',
        ]
        help_texts = {k:"" for k in fields}

class UserEditForm(UserCreationForm):
    email = forms.EmailField(label="Modificar Mail")
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["email", "password1", "password2"]
        help_texts = {k:"" for k in fields}

class AvatarForm(forms.Form):
    imagen = forms.ImageField()
    class Meta:
        model = Avatar
        fields = ['imagen']