import uuid
from django.db import models


class Flan(models.Model):
    flan_uuid = models.UUIDField()
    name = models.CharField(max_length=64)
    description = models.TextField()
    image_url = models.URLField()
    slug = models.SlugField()
    is_private = models.BooleanField()

class ContactForm(models.Model):
    contact_form_uuid = models.UUIDField(default=uuid.uuid4, editable=False )
    customer_email = models.EmailField()
    customer_name = models.CharField(max_length=64)
    message = models.TextField()
    
class Location(models.Model):
    name = models.CharField(max_length=250, verbose_name='Nombre sucursal')
    address = models.CharField(max_length=250, verbose_name='Dirección')
    lat = models.FloatField(verbose_name='Latitud')
    lng = models.FloatField(verbose_name='Longitud')

    class Meta:
        verbose_name = 'Sucursal'
        verbose_name_plural = 'Sucursales'
        ordering = ['name']

    def __str__(self) -> str:
        return self.name
