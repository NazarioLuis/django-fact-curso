from django.db import models
from base.models import ModeloBase 

# Create your models here.
class Proveedor(ModeloBase):
    descripcion = models.CharField(max_length=100,unique=True,verbose_name="Descripción")
    direccion = models.CharField(max_length=250,null=True,blank=True,verbose_name="Dirección")
    contacto = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20,null=True,blank=True,verbose_name="Teléfono")
    email = models.EmailField(max_length=254,null=True,blank=True,verbose_name="E-Mail")
    
    class Meta:
        verbose_name = "Proveedor"
        verbose_name_plural = "Proveedores"