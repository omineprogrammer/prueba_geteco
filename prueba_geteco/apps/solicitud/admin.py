from django.contrib import admin
from .models import Empresa, Ciudad, Registro


@admin.register(Empresa, Ciudad, Registro)
class RegistroAppAdmin(admin.ModelAdmin):
    pass
