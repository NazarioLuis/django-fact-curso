from django.db import models
from base.models import ModeloBase 

class Categoria(ModeloBase):
    descripcion = models.CharField(max_length=100,verbose_name="Descripción",help_text="Descripción de la categoría", unique=True)
    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"

    def __str__(self):
        return self.descripcion

class SubCategoria(ModeloBase):
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT,verbose_name="Categoría",
                limit_choices_to={'estado': True},) 
    descripcion = models.CharField(max_length=100,verbose_name="Descripción",help_text="Descripción de la sub categoría")
    class Meta:
        unique_together = ('categoria','descripcion',)
        verbose_name = "Sub Categoría"
        verbose_name_plural = "Sub Categorías"

    def __str__(self):
        return '{} ({})'.format(self.descripcion,self.categoria.descripcion)

class Marca(ModeloBase):
    descripcion = models.CharField(max_length=100,verbose_name="Descripción",help_text="Descripción de la marca", unique=True)
    class Meta:
        verbose_name = "Marca"
        verbose_name_plural = "Marcas"

    def __str__(self):
        return self.descripcion

class UnidadMedida(ModeloBase):
    descripcion = models.CharField(max_length=100,verbose_name="Descripción",help_text="Descripción de Unidad de Medida", unique=True)
    class Meta:
        verbose_name = "Unidad de Medida"
        verbose_name_plural = "Unidades de Medida"

    def __str__(self):
        return self.descripcion

class Producto(ModeloBase):
    codigo = models.CharField(max_length=20,verbose_name="Código", unique=True)
    codigo_barra = models.CharField(max_length=50,verbose_name="Código de barra", unique=True)
    descripcion = models.CharField(max_length=200,verbose_name="Descripción",help_text="Descripción del Producto")
    precio = models.FloatField(verbose_name="Precio venta", default=0)
    existencia = models.IntegerField(default=0)
    ultima_compra = models.DateField(null=True,blank=True)
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT)
    unidad_medida = models.ForeignKey(UnidadMedida, verbose_name="Unidad de medida", on_delete=models.PROTECT)
    subcategoria= models.ForeignKey(SubCategoria, verbose_name="Sub Categoría", on_delete=models.PROTECT)
    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"

    def __str__(self):
        return "[{}] {}".format(self.codigo,self.descripcion)