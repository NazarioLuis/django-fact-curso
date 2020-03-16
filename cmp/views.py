from base.views import BaseListView, BaseCreateView, BaseUpdateView, BaseDeleteView
from .models import Proveedor
from .forms import ProveedorForm
from .tables import ProveedorTable
from .filters import ProveedorFilter

#Vistas de Proveedores 
class ProveedorListView(BaseListView):
    model = Proveedor
    table_class = ProveedorTable
    filterset_class = ProveedorFilter

class ProveedorCreateView(BaseCreateView):
    model = Proveedor
    form_class=ProveedorForm
    def form_valid(self, form):
        form.instance.usuario_creacion = self.request.user
        return super().form_valid(form)

class ProveedorUpdateView(BaseUpdateView):
    model = Proveedor
    form_class=ProveedorForm
    def form_valid(self, form):
        form.instance.usuario_modificacion = self.request.user.id
        return super().form_valid(form)

class ProveedorDeleteView(BaseDeleteView):
    model = Proveedor
