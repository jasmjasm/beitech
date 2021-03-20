from django.contrib import admin
from .models import *
from .abstract import InfoComunAdmin


class ClienteAdmin(InfoComunAdmin):
    list_display = InfoComunAdmin.list_display + \
        ('apellido', 'cedula', 'nacimiento', 'talla')
    search_fields = InfoComunAdmin.search_fields + \
        ('apellido', 'cedula', 'nacimiento', 'talla')


class ArticuloAdmin(InfoComunAdmin):
    list_display = InfoComunAdmin.list_display + ('precio',)
    search_fields = InfoComunAdmin.search_fields + ('precio',)


class FacturaDetalleInLine(admin.TabularInline):
    model = FacturaDetalle
    fields = ('articulo', 'cantidad')


class FacturaAdmin(admin.ModelAdmin):
    list_display = ('id', 'fecha', 'cliente', 'es_de_hoy')
    search_fields = ('fecha', 'cliente')
    inlines = [
        FacturaDetalleInLine
    ]


admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Factura, FacturaAdmin)
admin.site.register(Articulo, ArticuloAdmin)
