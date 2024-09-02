from django.db import models
from django.contrib.auth.models import User
from libros.models import Libro

# Create your models here.
class prestamo(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    libro   = models.ForeignKey(Libro, on_delete=models.CASCADE)
    fecha_prestamo = models.DateField(auto_now_add=True)
    fecha_devolver = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.usuario.username} - {self.libro.titulo}"
