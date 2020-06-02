from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Pedidos(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    cliente = models.ForeignKey('clientes.Clientes', on_delete=models.DO_NOTHING)
    total = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return str(self.cliente)


class DetallePedido(models.Model):
    pedido = models.ForeignKey(Pedidos, on_delete=models.CASCADE)
    producto = models.ForeignKey('productos.Productos', on_delete=models.DO_NOTHING)
    cantidad = models.IntegerField(default=0)
    sub_total = models.DecimalField(max_digits=6, decimal_places=2, default=0)

    def __str__(self):
        return self.pedido

    def calcular_subtotal(self):
        pass
