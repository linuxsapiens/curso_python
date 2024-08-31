from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=200)
    complete = models.BooleanField(default=False)

    def __str__(self):
        terminada = "Incompleta"
        if self.complete:
            terminada = "Terminada"
        return self.title + ' - ' + terminada
    