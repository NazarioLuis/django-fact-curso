from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.db.models import ProtectedError
from django.db.utils import IntegrityError
from django.contrib import messages
from django.views.generic import TemplateView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django_tables2 import SingleTableMixin
from django_filters.views import FilterView


class Home(LoginRequiredMixin, TemplateView):
    template_name = "base/home.html"
    login_url="base:login"


class BaseListView(LoginRequiredMixin, SingleTableMixin, FilterView):
    template_name = "base/base_list.html"
    table_pagination = {
        "per_page": 20
    }
    login_url = "base:login"

class BaseCreateView(LoginRequiredMixin,CreateView):
    template_name = "base/base_form.html"
    login_url = "base:login"

    def __init__(self):
        if self.model: self.success_url=reverse_lazy(self.model._meta.app_label+":"+self.model.__name__.lower()+"_list")

class BaseUpdateView(LoginRequiredMixin,UpdateView):
    readonly = False
    template_name = "base/base_form.html"
    context_object_name = "obj"
    login_url = "base:login"

    def __init__(self, *args, **kwargs):
        if 'readonly' in kwargs: self.extra_context = {"readonly":kwargs['readonly']}
        if self.model: self.success_url=reverse_lazy(self.model._meta.app_label+":"+self.model.__name__.lower()+"_list")

        
class BaseDeleteView(LoginRequiredMixin,DeleteView):
    template_name = "base/base_delete.html"
    context_object_name = "obj"
    login_url = "base:login"

    def __init__(self):
        if self.model: self.success_url=reverse_lazy(self.model._meta.app_label+":"+self.model.__name__.lower()+"_list")

    def post(self, request, *args, **kwargs):
        try:
            return self.delete(request, *args, **kwargs)
        except Exception as e:
            if type(e) == ProtectedError: messages.error(request, 'No se puede eliminar, el registro se encuentra en uso!')
            else: messages.error(request, 'Se produjo un error inesperado.')
            return render(request, template_name=self.template_name, context=self.get_context_data())
