from django.contrib import admin
from sala_desenho.models import SalaDesenho

@admin.register(SalaDesenho)
class SalaDesenhoAdmin(admin.ModelAdmin):
    list_display = ('sala', 'qtd_cadeiras_desenho', 'materiais_disponiveis')