from django.contrib import admin
from laboratorio.models import Laboratorio

@admin.register(Laboratorio)
class LaboratorioAdmin(admin.ModelAdmin):
    list_display = ('sala', 'qtd_maquinas', 'softwares')