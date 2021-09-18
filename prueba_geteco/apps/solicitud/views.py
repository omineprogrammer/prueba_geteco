from prueba_geteco.core.views import *
from django.urls import reverse_lazy
from .forms import *
from .models import *


# Registro
class RegistroListView(BaseListView):
    model = Registro


class RegistroCreateView(BaseCreateView):
    model = Registro
    form_class = RegistroForm
    success_url = reverse_lazy(
        f'{model._meta.app_label}:{model._meta.verbose_name}-list')


class RegistroUpdateView(BaseDetailView):
    model = Registro
    form_class = RegistroForm
    success_url = reverse_lazy(
        f'{model._meta.app_label}:{model._meta.verbose_name}-list')


class RegistroDeleteView(BaseDeleteView):
    model = Registro
    success_url = reverse_lazy(
        f'{model._meta.app_label}:{model._meta.verbose_name}-list')


# Ciudad
class CiudadListView(BaseListView):
    model = Ciudad


class CiudadCreateView(BaseCreateView):
    model = Ciudad
    form_class = CiudadForm
    success_url = reverse_lazy(
        f'{model._meta.app_label}:{model._meta.verbose_name}-list')



class CiudadUpdateView(BaseDetailView):
    model = Ciudad
    form_class = CiudadForm
    success_url = reverse_lazy(
        f'{model._meta.app_label}:{model._meta.verbose_name}-list')


class CiudadDeleteView(BaseDeleteView):
    model = Ciudad
    success_url = reverse_lazy(
        f'{model._meta.app_label}:{model._meta.verbose_name}-list')


# Empresa
class EmpresaListView(BaseListView):
    model = Empresa


class EmpresaCreateView(BaseCreateView):
    model = Empresa
    form_class = EmpresaForm
    success_url = reverse_lazy(
        f'{model._meta.app_label}:{model._meta.verbose_name}-list')



class EmpresaUpdateView(BaseDetailView):
    model = Empresa
    form_class = EmpresaForm
    success_url = reverse_lazy(
        f'{model._meta.app_label}:{model._meta.verbose_name}-list')


class EmpresaDeleteView(BaseDeleteView):
    model = Empresa
    success_url = reverse_lazy(
        f'{model._meta.app_label}:{model._meta.verbose_name}-list')


