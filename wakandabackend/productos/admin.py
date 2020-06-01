from django.contrib import admin
from . models import TipoProducto, Productos, LineaProducto


class TipoProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio_mayorista', 'precio_final')


class ProductoAdmin(admin.ModelAdmin):
    list_display = ('aroma', 'tipo', 'linea')


admin.site.register(TipoProducto, TipoProductoAdmin)
admin.site.register(Productos, ProductoAdmin)
admin.site.register(LineaProducto)
