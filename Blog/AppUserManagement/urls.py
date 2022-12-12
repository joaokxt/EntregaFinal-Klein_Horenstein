from django.urls import path
from AppUserManagement import views

urlpatterns = [
    path('login/',views.AdminLoginView.as_view(), name="login"),
    path('signup/', views.SignupView.as_view(), name="signup"),
    path('add_avatar/', views.agregar_avatar, name="agregar_avatar"),
    path("logout/", views.AdminLogoutView.as_view(), name="logout"),
    path("edit_profile", views.editar_perfil, name="editar_perfil"),
    path("edit_bio", views.editar_bio, name="editar_bio"),
    path("profile/", views.mi_perfil, name="mi_perfil"),
    path("show_profile/<blog_autor>/", views.mostrar_usuario, name="usuario")
]

