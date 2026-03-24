# Create your models here.
from django.db import models
from django.utils import timezone

# Create your models here.
class Course(models.Model):
    title = models.CharField(
        verbose_name='Nombre del curso',
        max_length=200
    )
    content = models.TextField(
        verbose_name='Contenido del curso'
    )
    author = models.CharField(
        verbose_name='Docente del curso',
        max_length=100
    )
    call_link = models.URLField(
        verbose_name='Enlace de agendado',
    )
    created_at = models.DateTimeField(
        verbose_name='Creado el: ',
        default=timezone.now
    )

    def __str__(self):
        return self.title