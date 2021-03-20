from django.db import models
from django.contrib import admin


class InfoComun(models.Model):
    nombre = models.CharField(_("nombre"), max_length=50)
    activo = models.BooleanField(_("activo"), default=True)

    def __unicode__(self):
        return self.nombre

    class Meta:
        abstract = True
        ordering = ["nombre"]


# clase abstracta con informacion comun para admin
class InfoComunAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'activo',)
    list_display_links = ('nombre',)
    list_filter = ('activo',)
    search_fields = ('nombre',)
