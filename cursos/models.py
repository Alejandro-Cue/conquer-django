# Create your models here.
from django.db import models
from django.utils import timezone
from thumbnails.fields import ImageField
from ckeditor.fields import RichTextField

# Create your models here.
class Course(models.Model):
    title = models.CharField(
        verbose_name='Nombre del curso',
        max_length=200
    )
    content = RichTextField(
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

    show_home = models.BooleanField(
        verbose_name='Mostrar en Home',
        default=False
    )
    
    toc = models.FileField(
        verbose_name='Índice del curso',
        upload_to='course_toc/',
        null=True,
        blank=True
    )

    course_image = ImageField(
        verbose_name='Imagen del curso',
        upload_to='cursos/images/',
        null=True,
        blank=True
    )

    def __str__(self):
        return self.title