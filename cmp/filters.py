import django_filters
from .models import Proveedor

class ProveedorFilter(django_filters.FilterSet):
    descripcion = django_filters.CharFilter(lookup_expr='unaccent__icontains',label="Descripción: ")
    estado = django_filters.BooleanFilter(label="Activo: ")
    class Meta:
        model = Proveedor
        fields = ['descripcion','estado' ]