from django.contrib import admin
from predio_dep.models import PredioDep

@admin.register(PredioDep)
class PredioDepAdmin(admin.ModelAdmin):
    list_display = ('id_dep', 'id_predio')