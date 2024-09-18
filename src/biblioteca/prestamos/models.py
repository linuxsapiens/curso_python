from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from libros.models import Libro

User = get_user_model()

STATUS_CHOICES = [
    ('solicitado', 'Solicitado'),
    ('en_proceso', 'En Proceso'),
    ('prestado', 'Prestado'),
    ('devuelto', 'Devuelto'),
]

class Prestamo(models.Model):
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_prestamo = models.DateField(auto_now_add=True)
    fecha_devolucion = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='solicitado')

    def __str__(self):
        return f"{self.libro.titulo} - {self.usuario.username}"

@receiver(post_save, sender=Prestamo)
def actualizar_estado_libro(sender, instance, **kwargs):
    libro = instance.libro
    if instance.status == 'devuelto':
        libro.status = 'disponible'
    elif instance.status == 'solicitado':
        libro.status = 'reservado'
    elif instance.status == 'en_proceso':
        libro.status = 'reservado'
    else:
        libro.status = 'prestado'
    libro.save()    