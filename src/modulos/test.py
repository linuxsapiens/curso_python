# Modulos.- Permite reutilizar código ( funciones, clases, etc ) en un programa o script sin tener que copiar codigo, contienen:
#   Definiciones y declaraciones
#   Se pueden organizar en paquetes y subpaquetes
#   Se pueden importar solo cuando es necesario
# * Usar visual studio code

# Asi se importan las definiciones de un modulo, se deben llamar a ejecutar mediante el nombre y la funcion
# import saludos

# Este importa solo la funcion saludar
# from saludos import saludar

# Este importa todas las funciones y clases
# from saludos import *

# Ya se considera un paquete
from mensajes.hola.saludos import *
from mensajes.adios.despedidas import *

# imprime el nombre del modulo actual (main ya que es el programa principal)
# print(__name__)

# saludos.saludar()
saludar()

saludo = Saludo()

despedir()
despedida = Despedida()