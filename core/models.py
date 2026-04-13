from django.db import models
from django.utils import timezone

# Create your models here.
class Contact(models.Model):
    nombre = models.CharField(
        verbose_name='Nombre del contacto',
        max_length=100
    )
    email = models.EmailField(
        verbose_name='Email del contacto',
        max_length=100
    )
    comentario = models.TextField(
        verbose_name='Comentario del contacto'
    )
    created_at = models.DateTimeField(
        verbose_name='Fecha de creación: ',
        default=timezone.now
    )
    contactado = models.BooleanField(
        verbose_name='¿Se ha contactado al cliente?',
        default=False
    )
    def __str__(self):
        return self.nombre