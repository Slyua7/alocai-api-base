from django.contrib import admin
from predio.models import Predio

@admin.register(Predio)
class PredioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'id_endereco_predio')