import django_filters
from .models import Categoria,SubCategoria,Marca,UnidadMedida,Producto

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

class ProductoFilter(django_filters.FilterSet):
    descripcion = django_filters.CharFilter(lookup_expr='unaccent__icontains',label="Descripción: ")
    subcategoria__descripcion = django_filters.CharFilter(lookup_expr='unaccent__icontains',label="Sub Categorias: ")
    subcategoria__categoria__descripcion = django_filters.CharFilter(lookup_expr='unaccent__icontains',label="Categorias: ")
    estado = django_filters.BooleanFilter(label="Activo: ")
    class Meta:
        model = Producto
        fields = ['descripcion','subcategoria__categoria__descripcion','subcategoria__descripcion','estado' ]

class UnidadMedidaFilter(django_filters.FilterSet):
    descripcion = django_filters.CharFilter(lookup_expr='unaccent__icontains',label="Descripción: ")
    estado = django_filters.BooleanFilter(label="Activo: ")
    class Meta:
        model = UnidadMedida
        fields = ['descripcion','estado' ]

class SubCategoriaFilter(django_filters.FilterSet):
    descripcion = django_filters.CharFilter(lookup_expr='unaccent__icontains',label="Descripción: ")
    categoria__descripcion = django_filters.CharFilter(lookup_expr='unaccent__icontains',label="Categorias: ")
    estado = django_filters.BooleanFilter(label="Activo: ")
    class Meta:
        model = SubCategoria
        fields = ['descripcion','categoria__descripcion','estado' ]