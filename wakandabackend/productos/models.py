from django.db import models


class TipoProducto(models.Model):
    nombre = models.CharField(max_length=20)
    precio_mayorista = models.IntegerField(default=0)
    precio_final = models.IntegerField(default=0)

    def __str__(self):
        return self.nombre


class LineaProducto(models.Model):
    nombre = models.CharField(max_length=40)

    def __str__(self):
        return self.nombre


class Productos(models.Model):
    aroma = models.CharField(max_length=30, null=False, blank=False)
    tipo = models.ForeignKey(TipoProducto, on_delete=models.CASCADE)
    linea = models.ForeignKey(LineaProducto, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.aroma
