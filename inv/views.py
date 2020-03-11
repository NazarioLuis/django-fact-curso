from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView,UpdateView,DeleteView

from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Categoria,SubCategoria
from .forms import CategoriaForm,SubCategoriaForm 
from .tables import CategoriaTable,SubCategoriaTable
from .filters import CategoriaFilter,SubCategoriaFilter

from django_tables2 import SingleTableMixin
from django_filters.views import FilterView

#Vistas de Categorias 
class CategoriaListView(LoginRequiredMixin, SingleTableMixin, FilterView):
    template_name = "base/base_list.html"
    model = Categoria
    table_class = CategoriaTable
    filterset_class = CategoriaFilter
    table_pagination = {
        "per_page": 20
    }
    login_url = "base:login"

class CategoriaCreateView(LoginRequiredMixin,CreateView):
    model = Categoria
    template_name = "base/base_form.html"
    form_class=CategoriaForm
    success_url=reverse_lazy("inv:categoria_list")
    login_url = "base:login"

    def form_valid(self, form):
        form.instance.usuario_creacion = self.request.user
        return super().form_valid(form)

class CategoriaUpdateView(LoginRequiredMixin,UpdateView):
    readonly = False
    model = Categoria
    template_name = "base/base_form.html"
    context_object_name = "obj"
    form_class=CategoriaForm
    success_url=reverse_lazy("inv:categoria_list")
    login_url = "base:login"

    def __init__(self, *args, **kwargs):
        if 'readonly' in kwargs: self.extra_context = {"readonly":kwargs['readonly']}

    def form_valid(self, form):
        form.instance.usuario_modificacion = self.request.user.id
        return super().form_valid(form)


class CategoriaDeleteView(LoginRequiredMixin,DeleteView):
    model = Categoria
    template_name = "base/base_delete.html"
    context_object_name = "obj"
    success_url=reverse_lazy("inv:categoria_list")
    login_url = "base:login"


#Vistad de subcategorias
class SubCategoriaListView(LoginRequiredMixin, SingleTableMixin, FilterView):
    template_name = "base/base_list.html"
    model = SubCategoria
    table_class = SubCategoriaTable
    filterset_class = SubCategoriaFilter
    table_pagination = {
        "per_page": 20
    }
    login_url = "base:login"

class SubCategoriaCreateView(LoginRequiredMixin,CreateView):
    model = SubCategoria
    template_name = "base/base_form.html"
    form_class=SubCategoriaForm
    success_url=reverse_lazy("inv:subcategoria_list")
    login_url = "base:login"

    def form_valid(self, form):
        form.instance.usuario_creacion = self.request.user
        return super().form_valid(form)

class SubCategoriaUpdateView(LoginRequiredMixin,UpdateView):
    readonly = False
    model = SubCategoria
    template_name = "base/base_form.html"
    context_object_name = "obj"
    form_class=SubCategoriaForm
    success_url=reverse_lazy("inv:subcategoria_list")
    login_url = "base:login"

    def __init__(self,*args, **kwargs):
        if 'readonly' in kwargs: self.extra_context = {"readonly":kwargs['readonly']}

    def form_valid(self, form):
        form.instance.usuario_modificacion = self.request.user.id
        return super().form_valid(form)

class SubCategoriaDeleteView(LoginRequiredMixin,DeleteView):
    model = SubCategoria
    template_name = "base/base_delete.html"
    context_object_name = "obj"
    success_url=reverse_lazy("inv:subcategoria_list")
    login_url = "base:login"