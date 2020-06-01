from django.db import models
from datetime import datetime
from django.utils import timezone


class Pedidos(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    cliente = models.ForeignKey('clientes.Clientes', on_delete=models.DO_NOTHING)
    total = models.FloatField(default=0)

    def __str__(self):
        return str(self.cliente)


class DetallePedido(models.Model):
    pedido = models.ForeignKey(Pedidos, on_delete=models.CASCADE)
    producto = models.ForeignKey('productos.Productos', on_delete=models.DO_NOTHING)
    cantidad = models.IntegerField(default=0)
    precio = models.IntegerField(default=0)

    def __str__(self):
        return self.pedido

