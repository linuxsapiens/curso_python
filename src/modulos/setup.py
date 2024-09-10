# Crear una configuracion para setuptools
# https://setuptools.readthedocs.io/en/latest/setuptools.html

from setuptools import setup
setup(
  name='Mensajes',
  version='2.0',
  description='Un paquete para saludar y despedir',
  author='Gera Luis',
  author_email='hola@hola.com',
  url='python.org',
  packages=['mensajes', 'mensajes.hola', 'mensajes.adios'],
  scripts=['test.py'],
)

# Ejecutar: python3 setup.py sdist
# Genera la carpeta dist que contiene el paquete con extension tar.gz

# Entrando a la carpeta dist
# ejecutar: pip install Mensajes-1.0.tar.gz
# python3 -m pip install dist/Mensajes-1.0.tar.gz
# !pip list

#  despues de un cambio
# pip install Mensajes-2.0.tar.gz --upgrade

# pip uninstall Mensajes-2.0.tar.gz

# from setuptools import find_packages
# from setuptools import Extension
# from setuptools.command.build_ext import build_ext