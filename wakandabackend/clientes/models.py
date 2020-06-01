from django.db import models


class TiposDeCliente(models.Model):
    lista = (('Revendedor', 'Revendedor'), ('Comercio', 'Comercio'), ('Particular', 'Particular'))
    nombre = models.CharField(max_length=10, choices=lista)

    def __str__(self):
        return self.nombre


class Clientes(models.Model):
    nombre = models.CharField(max_length=30, null=False, blank=False)
    tipo = models.ForeignKey(TiposDeCliente, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre