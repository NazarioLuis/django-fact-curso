import django_filters
from .models import Categoria,SubCategoria,Marca

class MarcaFilter(django_filters.FilterSet):
    descripcion = django_filters.CharFilter(lookup_expr='unaccent__icontains',label="Descripción: ")
    estado = django_filters.BooleanFilter(label="Activo: ")
    class Meta:
        model = Marca
        fields = ['descripcion','estado' ]

class CategoriaFilter(django_filters.FilterSet):
    descripcion = django_filters.CharFilter(lookup_expr='unaccent__icontains',label="Descripción: ")
    estado = django_filters.BooleanFilter(label="Activo: ")
    class Meta:
        model = Categoria
        fields = ['descripcion','estado' ]

class SubCategoriaFilter(django_filters.FilterSet):
    descripcion = django_filters.CharFilter(lookup_expr='unaccent__icontains',label="Descripción: ")
    categoria__descripcion = django_filters.CharFilter(lookup_expr='unaccent__icontains',label="Categorias: ")
    estado = django_filters.BooleanFilter(label="Activo: ")
    class Meta:
        model = SubCategoria
        fields = ['descripcion','categoria__descripcion','estado' ]