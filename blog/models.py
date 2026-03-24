from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    title = models.CharField(
        verbose_name='Título',
        max_length=200
    )
    content = models.TextField(
        verbose_name='Contenido'
    )
    author = models.CharField(
        verbose_name='Autor',
        max_length=100
    )
    created_at = models.DateTimeField(
        verbose_name='Creado el: ',
        default=timezone.now
    )

    show_home = models.BooleanField(
        verbose_name='Mostrar en Home',
        default=False
    )

    def __str__(self):
        return self.title