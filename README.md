# EntregaFinal-Klein_Horenstein
Entrega final del curso de Python de Coder House. Hecho por João Klein Xavier Terck y Guido Horenstein

Moviespedia es una espécie de blog colaborativo, donde los usuarios registrados pueden escribir artículos dando su opinión sobre películas.
    - Cada artículo contiene:
        * Título de película y de reseña.
        * Fecha de lanzamiento de película y su duración en min.
        * Fecha de publicación y autor.
        * Reseña.
        * Género de película y calificación del autor en estrellas.
    - Los usuarios anónimos solo podrán leer los artículos.
    - La edición y el borrado de artículos solo es posible si el usuario es administrador. 

# Rol de cada participante
Guido Horenstein se encargó de:
    -Modelos y formularios para creación de blogs
    -Signup y login/out
    -Formularios edición de perfil
    -Búsqueda de blogs
João Terck se encargó de:
    -Funcionalidad de comentarios
    -Bio y avatar de usuario
    -Edición y apagado de Blogs
    -Filtrado de películas por género
    -Suba de imágenes
    -HTML


# Información para usuario
Hay 3 reseñas precargadas y el usuario admin es: [Username: Admin | Contraseña: administrador]

Para ejecutar el proyecto, una vez en el directorio del mismo se ejecutan los siguientes comandos en la terminal:

Instalar y ejecutar entorno virtual:

```bash
    C:\Users\joaok\Documents\A-PYTHON\Entrega\EntregaFinal-Klein_Horenstein> pip install virtualenv
```
```bash
    C:\Users\joaok\Documents\A-PYTHON\Entrega\EntregaFinal-Klein_Horenstein> python -m virtualenv venv
```
```bash
    C:\Users\joaok\Documents\A-PYTHON\Entrega\EntregaFinal-Klein_Horenstein> venv/Scripts/activate
```
```bash
    C:\Users\joaok\Documents\A-PYTHON\Entrega\EntregaFinal-Klein_Horenstein> cd Blog
```

Instalar los módulos necesarios:
```bash
    (venv)C:\Users\joaok\Documents\A-PYTHON\Entrega\EntregaFinal-Klein_Horenstein\Blog> pip install Django
```
```bash
    (venv)C:\Users\joaok\Documents\A-PYTHON\Entrega\EntregaFinal-Klein_Horenstein\Blog> pip install Pillow
```
```bash
    (venv)C:\Users\joaok\Documents\A-PYTHON\Entrega\EntregaFinal-Klein_Horenstein\Blog> pip install django-ckeditor
```

Ejecutar servidor:
```bash
    (venv)C:\Users\joaok\Documents\A-PYTHON\Entrega\EntregaFinal-Klein_Horenstein\Blog> python manage.py runserver
```

Y ahora solo acceder :fireworks:
```bash
    System check identified no issues (0 silenced).
    December 12, 2022 - 20:54:26
    Django version 4.1.3, using settings 'Blog.settings'
    Starting development server at http://127.0.0.1:8000/
    Quit the server with CTRL-BREAK.
```