from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    marca = models.CharField(max_length=255)
    precio = models.TextField()  

    def __str__(self):
        return self.nombre