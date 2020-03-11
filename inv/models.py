from django.db import models
from base.models import ModeloBase 

# Create your models here.
class Categoria(ModeloBase):
    descripcion = models.CharField(max_length=100,verbose_name="Descripción",help_text="Descripción de la categoría", unique=True)
    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"

    def __str__(self):
        return self.descripcion

    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Categoria, self).save()

# Create your models here.
class SubCategoria(ModeloBase):
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT,verbose_name="Categoría") 
    descripcion = models.CharField(max_length=100,verbose_name="Descripción",help_text="Descripción de la sub categoría")
    class Meta:
        unique_together = ('categoria','descripcion',)
        verbose_name = "Sub Categoría"
        verbose_name_plural = "Sub Categorías"

    def __str__(self):
        return '{} ({})'.format(self.descripcion,self.categoria.descripcion)

    def save(self):
        self.descripcion = self.descripcion.upper()
        super(SubCategoria, self).save()

