from django.contrib import admin
from .models import Pedidos, DetallePedido


class PedidosAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'fecha', 'total')


class DetallePedidoAdmin(admin.ModelAdmin):
    list_display = ('pedido', 'producto', 'cantidad')


admin.site.register(Pedidos, PedidosAdmin)
admin.site.register(DetallePedido, DetallePedidoAdmin)