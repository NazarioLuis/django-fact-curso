from django.urls import path
from .views import CategoriaCreateView,CategoriaUpdateView,CategoriaListView,CategoriaDeleteView,\
    SubCategoriaListView,SubCategoriaCreateView,SubCategoriaUpdateView,SubCategoriaDeleteView,\
    MarcaListView,MarcaCreateView,MarcaUpdateView,MarcaDeleteView
urlpatterns = [
    path('categorias/', CategoriaListView.as_view(),name='categoria_list'),
    path('categorias/new', CategoriaCreateView.as_view(),name='categoria_new'),
    path('categorias/edit/<int:pk>', CategoriaUpdateView.as_view(),name='categoria_edit'),
    path('categorias/delete/<int:pk>', CategoriaDeleteView.as_view(),name='categoria_delete'),
    path('categorias/view/<int:pk>', CategoriaUpdateView.as_view(readonly=True),name='categoria_view'),
    path('subcategorias/', SubCategoriaListView.as_view(),name='subcategoria_list'),
    path('subcategorias/new', SubCategoriaCreateView.as_view(),name='subcategoria_new'),
    path('subcategorias/edit/<int:pk>', SubCategoriaUpdateView.as_view(),name='subcategoria_edit'),
    path('subcategorias/delete/<int:pk>', SubCategoriaDeleteView.as_view(),name='subcategoria_delete'),
    path('subcategorias/view/<int:pk>', SubCategoriaUpdateView.as_view(readonly=True),name='subcategoria_view'),
    path('marcas/', MarcaListView.as_view(),name='marca_list'),
    path('marcas/new', MarcaCreateView.as_view(),name='marca_new'),
    path('marcas/edit/<int:pk>', MarcaUpdateView.as_view(),name='marca_edit'),
    path('marcas/delete/<int:pk>', MarcaDeleteView.as_view(),name='marca_delete'),
    path('marcas/view/<int:pk>', MarcaUpdateView.as_view(readonly=True),name='marca_view'),
]

app_name='inv'