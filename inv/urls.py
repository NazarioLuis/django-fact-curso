from django.urls import path
from .views import CategoriaCreateView,CategoriaUpdateView,CategoriaListView,CategoriaDeleteView,\
    SubCategoriaListView,SubCategoriaCreateView,SubCategoriaUpdateView,SubCategoriaDeleteView
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
]

app_name='inv'