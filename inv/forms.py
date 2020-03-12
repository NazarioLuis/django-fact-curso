from django import forms

from .models import Categoria,SubCategoria, Marca

class CategoriaForm(forms.ModelForm):
    
    class Meta:
        model = Categoria
        fields = ("descripcion","estado",)

class MarcaForm(forms.ModelForm):
    
    class Meta:
        model = Marca
        fields = ("descripcion","estado",)

class SubCategoriaForm(forms.ModelForm):
    
    class Meta:
        model = SubCategoria
        fields = ("descripcion","categoria","estado",)