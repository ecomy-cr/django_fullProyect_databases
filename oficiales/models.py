from enum import unique
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Reporte(models.Model):
    asunto = models.CharField(max_length=100)
    detalle = models.TextField(blank=False)
    created = models.DateTimeField(auto_now_add=True)
    importante = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.asunto + '-: ' + self.user.username
# Create your models here.

class Entrada(models.Model):
    ingreso = models.CharField(max_length=100)
    salida = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.Ingreso + '-: ' + self.user.username

class PerfilOf(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=100)
    puesto = models.CharField(max_length=100)
    codigo = models.CharField(max_length=100, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.codigo + '-: ' + self.user.username