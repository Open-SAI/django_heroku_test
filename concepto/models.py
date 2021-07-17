from django.db import models

# Create your models here.
class Concepto (models.Model):
    titulo = models.CharField(max_length=70, blank=False, default='')
    descripcion = models.CharField(max_length=200, blank=False, default='')
    published = models.BooleanField(default=False)


