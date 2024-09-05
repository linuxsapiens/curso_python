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

Antes de poder programar el préstamo de libros tenemos que implementar el manejo de usuarios y seguridad, para eso intentaremos usar el motor de usuarios que incluye django.

1. Incluir las rutas internas de django en core/urls.py `path('auth/', include('django.contrib.auth.urls')),`
2. La biblioteca interna contiene rutas definidas para las acciones de authorización de django en cuanto a usuarios
    ```plain
    auth/login/ [name='login']
    auth/logout/ [name='logout']
    auth/password_change/ [name='password_change']
    auth/password_change/done/ [name='password_change_done']
    auth/password_reset/ [name='password_reset']
    auth/password_reset/done/ [name='password_reset_done']
    auth/reset/<uidb64>/<token>/ [name='password_reset_confirm']
    auth/reset/done/ [name='password_reset_complete']
    ```
    1. Todas las rutas internamente manejan se dirijen a una carpeta FIJA llamada "registratio/n"
3. Crear la carpeta usuarios/registration y dentro la platilla "login.html"
    1. agregar la carpeta usuarios/templates en core/settings.py en la sección TEMPLATES
    2. Además es conveniente agregar una ruta a donde se redirija al usuario después de una entrada existosa ( login )
        1. En core/settings.py ir al final y poner
        ```plain
        LOGIN_REDIRECT_URL = "/"  # new 
        ```
    3. Ahora se podría hacer login en el sistema interno de python en la ruta [http://localhost:8000/auth/login](http://localhost:8000/auth/login)
4. Aún no es posible hacer login en el sistema por que es necesario crear un super usuario, detener el servidor y ejecutar:
    1. `python manage.py createsuperuser`
5. Ya se puede poner a ejecutar de nuevo el servidor y hacer login, si tiene éxito después de login se redirije al index " / "
6. Modificar el código de core/templates/home.html para insertar código que se ajuste al manejo de usuario loggeado
7. Ajustar el código de core/templates/includes/navbar.html para que se valide si esta el usuario loggeado o no.
    1. También hacer los ajustes en el menú desktop
8. Ahora vamos a agregar lo necesario para usar el mecanismo interno de registro de usuario
    1. Crear usuarios/urls.py e insertar el código para el registro de usuarios
    2. Crear las vistas de usuarios en usuarios/views.py
    3. Agregar en core/urls.py las rutas de usuarios/urls.py
    4. Crear ahora la plantilla para el registro de un nuevo usuario en usuarios
9. Al ejecutar el servidor ya sería posible registrar un nuevo usuario en /auth/registration/signup
10. Crear un usuario de prueba e intentar entrar con ese usuario a /admin para comprobar que no es posible por que el usuario creado es un usuario normal y no tiene permisos de super usuario.
11. Sería posible agregar el link anterior al template de login
    1. También agregar el link de "¿ Ya tienes cuenta ? Inicia sesión"
12. Repetir las operaciones anteriores para el cambio de contraseña
    1. usuarios/registration/password\_change\_form.html
    2. usuarios/registration/password\_change\_done.html

  

Después de esto ya se podría continuar con la implementación de los préstamos

