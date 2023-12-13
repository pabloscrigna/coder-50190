from django.db import models

class Hermano(models.Model):
    nombre = models.CharField(max_length=20)
    fechaNacimiento = models.DateField()
    comentario = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} - {self.fechaNacimiento} - {self.comentario}"
