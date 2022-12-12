from django.urls import path
from AppBlog.views import *

urlpatterns = [
    path('pages/<modo>/', mostrar_blogs, name="mostrar_blogs"),
    path('page/<blog_id>/', mostrar_blog, name="mostrar_blog"),
    path("edit_blog/<blog_id>/", editar_blog, name="editar_blog"),
    path("delete_blog/<blog_id>/", eliminar_blog, name="eliminar_blog"),
    path("create_blog/", crear_blog, name="crear_blog"),
    path("search/", buscar_blog, name="buscar"),
    path("genres/", mostrar_generos, name="generos"),
    path("genre/<genero_nombre>/", genero , name="genero"),
    path("about/", about_us, name="about_us"),
]

