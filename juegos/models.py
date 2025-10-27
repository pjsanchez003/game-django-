from django.db import models

class Juego(models.Model):
    nombre = models.CharField(max_length=100)
    genero = models.CharField(max_length=50)
    plataforma = models.CharField(max_length=50)
    fecha_lanzamiento = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.nombre
