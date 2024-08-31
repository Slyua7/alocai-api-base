from django.contrib import admin
from usuario.models import Usuario

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('user', 'nascimento', 'id_endereco_usuario', 'tipo')