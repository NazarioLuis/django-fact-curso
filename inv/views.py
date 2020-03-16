from base.views import BaseListView, BaseCreateView, BaseUpdateView, BaseDeleteView
from .models import Categoria,SubCategoria,Marca,UnidadMedida,Producto
from .forms import CategoriaForm,SubCategoriaForm,MarcaForm,UnidadMedidaForm,ProductoForm 
from .tables import CategoriaTable,SubCategoriaTable,MarcaTable,UnidadMedidaTable,ProductoTable
from .filters import CategoriaFilter,SubCategoriaFilter,MarcaFilter,UnidadMedidaFilter,ProductoFilter

#Vistas de Categorias 
class CategoriaListView(BaseListView):
    model = Categoria
    table_class = CategoriaTable
    filterset_class = CategoriaFilter

class CategoriaCreateView(BaseCreateView):
    model = Categoria
    form_class=CategoriaForm
    def form_valid(self, form):
        form.instance.usuario_creacion = self.request.user
        return super().form_valid(form)

class CategoriaUpdateView(BaseUpdateView):
    model = Categoria
    form_class=CategoriaForm
    def form_valid(self, form):
        form.instance.usuario_modificacion = self.request.user.id
        return super().form_valid(form)

class CategoriaDeleteView(BaseDeleteView):
    model = Categoria

#Vistad de subcategorias
class SubCategoriaListView(BaseListView):
    model = SubCategoria
    table_class = SubCategoriaTable
    filterset_class = SubCategoriaFilter

class SubCategoriaCreateView(BaseCreateView):
    model = SubCategoria
    form_class=SubCategoriaForm
    def form_valid(self, form):
        form.instance.usuario_creacion = self.request.user
        return super().form_valid(form)

class SubCategoriaUpdateView(BaseUpdateView):
    model = SubCategoria
    form_class=SubCategoriaForm
    def form_valid(self, form):
        form.instance.usuario_modificacion = self.request.user.id
        return super().form_valid(form)

class SubCategoriaDeleteView(BaseDeleteView):
    model = SubCategoria

#Vistas de Marca
class MarcaListView(BaseListView):
    model = Marca
    table_class = MarcaTable
    filterset_class = MarcaFilter

class MarcaCreateView(BaseCreateView):
    model = Marca
    form_class=MarcaForm
    def form_valid(self, form):
        form.instance.usuario_creacion = self.request.user
        return super().form_valid(form)

class MarcaUpdateView(BaseUpdateView):
    model = Marca
    form_class=MarcaForm
    def form_valid(self, form):
        form.instance.usuario_modificacion = self.request.user.id
        return super().form_valid(form)

class MarcaDeleteView(BaseDeleteView):
    model = Marca

#Vistas de Unidades de Medida
class UnidadMedidaListView(BaseListView):
    model = UnidadMedida
    table_class = UnidadMedidaTable
    filterset_class = UnidadMedidaFilter

class UnidadMedidaCreateView(BaseCreateView):
    model = UnidadMedida
    form_class=UnidadMedidaForm
    def form_valid(self, form):
        form.instance.usuario_creacion = self.request.user
        return super().form_valid(form)

class UnidadMedidaUpdateView(BaseUpdateView):
    model = UnidadMedida
    form_class=UnidadMedidaForm
    def form_valid(self, form):
        form.instance.usuario_modificacion = self.request.user.id
        return super().form_valid(form)

class UnidadMedidaDeleteView(BaseDeleteView):
    model = UnidadMedida

#Vistas de Productos
class ProductoListView(BaseListView):
    model = Producto
    table_class = ProductoTable
    filterset_class = ProductoFilter

class ProductoCreateView(BaseCreateView):
    model = Producto
    form_class=ProductoForm
    def form_valid(self, form):
        form.instance.usuario_creacion = self.request.user
        return super().form_valid(form)

class ProductoUpdateView(BaseUpdateView):
    model = Producto
    form_class=ProductoForm
    def form_valid(self, form):
        form.instance.usuario_modificacion = self.request.user.id
        return super().form_valid(form)

class ProductoDeleteView(BaseDeleteView):
    model = Producto