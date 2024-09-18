from django.db import models

STATUS_CHOICES = [
    ('disponible', 'Disponible'),
    ('prestado', 'Prestado'),
    ('reservado', 'Reservado'),
]

# Create your models here.
class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor  = models.CharField(max_length=200)
    isbn   = models.CharField(max_length=13, unique=True)
    fecha_publicacion = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='disponible')
    cover_image = models.ImageField(upload_to='book_covers/', null=True, blank=True)

    def __str__(self):
        return self.titulo
