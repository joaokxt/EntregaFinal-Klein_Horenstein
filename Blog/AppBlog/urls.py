from django.urls import path
from AppBlog.views import *

urlpatterns = [
    path('blogs/<modo>/', mostrar_blogs, name="mostrar_blogs"),
    path('blog/<blog_id>/', mostrar_blog, name="mostrar_blog"),
    path("editar_blog/<blog_id>/", editar_blog, name="editar_blog"),
    path("eliminar_blog/<blog_id>/", eliminar_blog, name="eliminar_blog"),
    path("crear_blog/", crear_blog, name="crear_blog"),
    path("buscar/", buscar_blog, name="buscar"),
    path("generos/", mostrar_generos, name="generos"),
    path("genero/<genero_nombre>/", genero , name="genero"),
    path("about_us/", about_us, name="about_us"),
]

