from django.db import models


class Clientes(models.Model):
    REVENDEDOR = 'R'
    COMERCIO = 'C'
    PARTICULAR = 'P'
    MAYORISTA = 'M'

    TIPO_CLIENTE = (
        (REVENDEDOR, 'Revendedor'),
        (COMERCIO, 'Comercio'),
        (PARTICULAR, 'Particular'),
        (MAYORISTA, 'Mayorista')
    )
    nombre = models.CharField(max_length=30, null=False, blank=False)
    tipo = models.CharField(max_length=1, choices=TIPO_CLIENTE, default=REVENDEDOR)

    # Agregar profile de usuario.

    def __str__(self):
        return self.nombre