# Proyecto biblioteca

1. Crear la carpeta del proyecto
2. Abrir visual studio code y abrir la carpeta del proyecto
    1. Si tienes windows establecer por default la terminal de comandos para que sea el "command prompt" y no el "power shell"
        1. CTRL+Shift+P
        2. Terminal: Select Default Profile
        3. Command prompt
3. Abrir una terminal ( se abrirá en la carpeta actual del proyecto )
4. Crear y activar el entorno virtual ( venv ) para el proyecto.
    ```bash
    # Windows
    python -m venv .venv
    # Linux / Mac
    . .venv/bin/activate
    # Windows
    .venv\Scripts\activate
    # Mac / Linux
    . .venv/bin/activate
    ```
5. Instalar Django para el proyecto actual
    1. `pip install django` El framework principal
    2. `pip install Pillow` Para el manejo de imágenes
    3. Ejecutar el módulo de administración de django para que cree la estructura inicial del proyecto que llamaremos "core"
    ```plain
    django-admin startproject core .
    ```
6. Crear las aplicaciones ( módulos ) para libros, usuarios y préstamos
    1. `django-admin startapp libros`
    2. 
7. Crear los modelos para cada una de las entidades de base de datos ( libros y préstamos )
    1. libros/models.py
    2. prestamos/models.py
8. Crear las tablas en la base de datos
    1. Para que se creen las migraciones es necesario agregar las apps en donde están declarados los modelos en core/settings INSTALLED\_APPS\[ \]
    2. crear los archivos de migración ( migrate ) `python manage.py makemigrations`
    3. ejecutar los archivos de migración `python manage.py migrate`
    4. Comprobar que se hayan creado las tablas con DB Browser for SQLite o DbSchema
9. Crear las carpetas para plantillas en core y en las aplicaciones, en cada una llamarlas "templates"
10. Mostrar la diapositiva 25
    1. El UI en python ha estado relegado por que no tiene tanta interactividad como JS pero hoy día está evolucionando con [htmx.org](http://htmx.org), django-cotton y librerías declarativas de JS como alpine js.
11. Crear las plantillas base en core/templates
12. Conectar las plantillas
    1. Agregar las carpetas de plantillas en core/settings.py TEMPLATES = \[ \]
    2. Agregar la ruta de static en core/settings.py
    3. Crear la función home en core/urls.py
13. Crear los templates en libros/templates
    1. Agregar la ruta en core/settings.py TEMPLATES = \[ \]
14. Crear el formulario en libros/forms.py
15. Crear [urls.py](http://urls.py) en libros/
    1. explicar como funciona la importación de urls desde aplicaciones django
    2. crear [urls.py](http://urls.py) e importarlo en core/urls.py agregando las rutas al final
16. Crear la carpeta media/book\_covers y configurar la en core/settings
17. Ejecutar el proyecto.