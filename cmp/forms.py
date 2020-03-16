from django import forms

from .models import Proveedor

class ProveedorForm(forms.ModelForm):
    def clean_descripcion(self):
        return str(self.cleaned_data['descripcion']).upper()
    class Meta:
        model = Proveedor
        fields = ("descripcion","direccion","contacto","telefono","email","estado",)