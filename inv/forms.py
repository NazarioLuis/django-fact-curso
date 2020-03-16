from django import forms

from .models import Categoria,SubCategoria,Marca,UnidadMedida,Producto

class CategoriaForm(forms.ModelForm):
    def clean_descripcion(self):
        return str(self.cleaned_data['descripcion']).upper()
    class Meta:
        model = Categoria
        fields = ("descripcion","estado",)

class MarcaForm(forms.ModelForm):
    def clean_descripcion(self):
        return str(self.cleaned_data['descripcion']).upper()
    class Meta:
        model = Marca
        fields = ("descripcion","estado",)

class SubCategoriaForm(forms.ModelForm):
    def clean_descripcion(self):
        return str(self.cleaned_data['descripcion']).upper()
    class Meta:
        model = SubCategoria
        fields = ("descripcion","categoria","estado",)

class UnidadMedidaForm(forms.ModelForm):
    def clean_descripcion(self):
        return str(self.cleaned_data['descripcion']).upper()
    class Meta:
        model = UnidadMedida
        fields = ("descripcion","estado",)

class ProductoForm(forms.ModelForm):
    def clean_codigo(self):
        return str(self.cleaned_data['codigo']).upper()
    def clean_descripcion(self):
        return str(self.cleaned_data['descripcion']).upper()
    def __init__(self,*args, **kwargs):
        super().__init__(*args,**kwargs)
        self.fields['existencia'].widget.attrs['readonly'] = True
        self.fields['ultima_compra'].widget.attrs['readonly'] = True
    class Meta:
        fields = ('codigo','codigo_barra','descripcion','subcategoria','marca','unidad_medida','precio','existencia','ultima_compra')
        model = Producto