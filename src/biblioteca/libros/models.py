from django.db import models

# Create your models here.
class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor  = models.CharField(max_length=200)
    isbn   = models.CharField(max_length=13, unique=True)
    fecha_publicacion = models.DateField()
    cover_image = models.ImageField(upload_to='book_covers/', null=True, blank=True)

    def __str__(self):
        return self.titulo
