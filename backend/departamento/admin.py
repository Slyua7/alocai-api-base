from django.contrib import admin
from departamento.models import Departamento

@admin.register(Departamento)
class DepartamentoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'universidade', 'area', 'coordenador')