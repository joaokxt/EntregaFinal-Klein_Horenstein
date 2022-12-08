from django.urls import path
from AppUserManagement import views

urlpatterns = [
    path('login/',views.AdminLoginView.as_view(), name="login"),
    path('signup/', views.SignupView.as_view(), name="signup"),
    path('agregar_avatar/', views.agregar_avatar, name="agregar_avatar"),
    path("logout/", views.AdminLogoutView.as_view(), name="logout"),
    path("editar_usuario/", views.editar_perfil, name="editar_perfil"),
    path("mi_perfil/", views.mi_perfil, name="mi_perfil"),
    path("mostrar_usuario/<blog_autor>/", views.mostrar_usuario, name="usuario")
]

