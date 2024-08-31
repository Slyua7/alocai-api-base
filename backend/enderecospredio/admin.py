from django.contrib import admin
from enderecospredio.models import EnderecosPredio

@admin.register(EnderecosPredio)
class EnderecosPredioAdmin(admin.ModelAdmin):
    list_display = ('cep', 'rua', 'numero')