from django.db import models
from .abstract import InfoComun
from .validators import valida_pdf
from django.utils.translation import ugettext as _


class ClienteManager(models.Manager):
    def clientes_activos(self):
        return self.get_queryset().filter(activo=True)

    def clientes_inactivos(self):
        return self.get_queryset().filter(activo=False)


# clase cliente que hereda de la clase abstracta infocomun
class Cliente(InfoComun):

    # selecciones
    TALLAS_CHOICES = (
        ('1', 'XS'),
        ('2', 'S'),
        ('3', 'M'),
        ('4', 'L'),
        ('5', 'XL'),
    )

    apellido = models.CharField(_("apellido"), max_length=50)
    cedula = models.IntegerField(_("cedula"), unique=True)
    nacimiento = models.DateField(
        _("nacimiento"), null=True, blank=True, help_text="AAAA-MM-DD")
    talla = models.CharField(_('talla'), max_length=1,
                             choices=TALLAS_CHOICES, blank=True)
    rut = models.FileField(_("RUT"), validators=[
                           valida_pdf], blank=True, upload_to='static/rut/')

    objects = ClienteManager()

    # propiedad obtiene el nombre completo
    def _get_nombre_completo(self):
        return '%s %s' % (self.nombre, self.apellido)
    nombre_completo = property(_get_nombre_completo)

    # sobreescribe el metodo guardar
    def save(self, *args, **kwargs):
        super(Cliente, self).save(*args, **kwargs)

    # sobreescribe el metodo eliminar
    def delete(self, *args, **kwargs):
        super(Cliente, self).delete(*args, **kwargs)

    class Meta(InfoComun.Meta):
        verbose_name_plural = _('clientes')


# clase tipo proxy que extiende funcionalidad de la clase padre
class ClienteOrdenadoDesc(Cliente):

    def _get_longitud_apellido(self):
        return len(self.apellido)

    class Meta:
        ordering = ["-apellido"]
        proxy = True


class Articulo(InfoComun):
    precio = models.IntegerField(_("precio"), default=0)

    class Meta(InfoComun.Meta):
        verbose_name_plural = _('articulos')


class Factura(models.Model):
    cliente = models.ForeignKey(Cliente)
    fecha = models.DateField(blank=False, null=False)

    def __unicode__(self):
        return u'%s %s' % (self.id, self.fecha)

    # metodo personalizado dentro de modelo
    def es_de_hoy(self):
        from datetime import date
        if self.fecha == date.today():
            return "si"
        else:
            return "no"

    class Meta:
        verbose_name_plural = _('facturas')


class FacturaDetalle(models.Model):
    factura = models.ForeignKey(Factura)
    articulo = models.ForeignKey(Articulo)
    cantidad = models.IntegerField()

    def __unicode__(self):
        return u'%s' % self.articulo
