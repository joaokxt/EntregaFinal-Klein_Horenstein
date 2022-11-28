from django.urls import path
from AppBlog import views

urlpatterns = [
    path('login/',views.AdminLoginView.as_view(), name="login"),
    path('signup/', views.SignupView.as_view(), name="signup"),
    path("generos/", views.mostrar_generos, name="mostrar_generos"),
    path("accion/", views.accion , name="accion"),
    path("drama/", views.drama , name="drama"),
    path("terror/", views.terror , name="terror"),
    path("ciencia_ficcion/", views.ciencia_ficcion , name="ciencia_ficcion"),
    path("comedia/", views.comedia , name="comedia"),
    path("drama/", views.drama , name="drama"),
    path("fantasia/", views.fantasia , name="fantasia"),
    path("about/", views.about_us, name="about_us"),
    path("logout/", views.AdminLogoutView.as_view(), name="logout"),
    path("cargar_resenia/", views.crear_blog, name="crear_resenia")
]