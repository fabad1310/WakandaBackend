from django.contrib import admin
from . models import Clientes, TiposDeCliente


class TiposDeClienteAdmin(admin.ModelAdmin):
    list_display = ['nombre']


class ClientesAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'tipo')


admin.site.register(TiposDeCliente, TiposDeClienteAdmin)
admin.site.register(Clientes, ClientesAdmin)
