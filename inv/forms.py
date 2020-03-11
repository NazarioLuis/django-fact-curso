from django import forms

from .models import Categoria,SubCategoria

class CategoriaForm(forms.ModelForm):
    
    class Meta:
        model = Categoria
        fields = ("descripcion","estado",)

class SubCategoriaForm(forms.ModelForm):
    
    class Meta:
        model = SubCategoria
        fields = ("descripcion","categoria","estado",)