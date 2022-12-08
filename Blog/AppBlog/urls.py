from django.urls import path
from AppBlog import views

urlpatterns = [
    path('pages/', views.mostrar_blogs, name="mostrar_blogs"),
    path('pages/<blog_id>/', views.mostrar_blog, name="mostrar_blog"),
    path("editar_blog/<blog_id>/", views.editar_blog, name="editar_blog"),
    path("eliminar_blog/<blog_id>/", views.eliminar_blog, name="eliminar_blog"),
    path("crear_resenia/", views.crear_blog, name="crear_resenia"),
    path("buscar/", views.buscar_blog, name="buscar"),
    path("generos/", views.mostrar_generos, name="generos"),
    path("genero/<genero_nombre>/", views.genero , name="genero"),
    path("about_us/", views.about_us, name="about_us"),
]

