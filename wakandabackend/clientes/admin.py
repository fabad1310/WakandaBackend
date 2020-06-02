from django.contrib import admin
from . models import Clientes


class ClientesAdmin(admin.ModelAdmin):
    list_display = ['tipo', 'usuario']
    list_filter = ('tipo', )
    list_select_related = ('usuario', )


admin.site.register(Clientes, ClientesAdmin)
