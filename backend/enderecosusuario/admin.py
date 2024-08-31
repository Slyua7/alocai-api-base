from django.contrib import admin
from enderecosusuario.models import EnderecosUsuario

@admin.register(EnderecosUsuario)
class EnderecosUsuarioAdmin(admin.ModelAdmin):
    list_display = ('cep', 'rua', 'numero')