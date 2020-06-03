from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save

User = get_user_model()


class Clientes(models.Model):
    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

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

    usuario = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True)
    tipo = models.CharField(max_length=1, choices=TIPO_CLIENTE, default=REVENDEDOR)
    telefono = models.IntegerField(max_length=25)
    fecha_de_nacimiento = models.DateField(auto_now=True)
    domicilio = models.CharField(max_length=150)
    referencia = models.CharField(max_length=200, help_text="Como nos conociste?")
    # Agregar profile de usuario: (domicilio, telefono, etc)

    def __str__(self):
        return self.nombre

    @classmethod
    def relacionar_usuario_cliente(cls, **kwargs):
        cliente = None
        if kwargs['created']:
            cliente = cls.objects.create(
                usuario=kwargs['instance'],
            )

        return cliente


post_save.connect(sender=User, receiver=Clientes.relacionar_usuario_cliente)
