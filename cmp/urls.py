from django.urls import path
from .views import ProveedorCreateView,ProveedorUpdateView,ProveedorListView,ProveedorDeleteView
    
urlpatterns = [
    path('proveedores/',ProveedorListView.as_view(),name='proveedor_list'),
    path('proveedores/new',ProveedorCreateView.as_view(),name='proveedor_new'),
    path('proveedores/edit/<int:pk>',ProveedorUpdateView.as_view(),name='proveedor_edit'),
    path('proveedores/delete/<int:pk>',ProveedorDeleteView.as_view(),name='proveedor_delete'),
    path('proveedores/view/<int:pk>',ProveedorUpdateView.as_view(readonly=True),name='proveedor_view'),
]

app_name='cmp'