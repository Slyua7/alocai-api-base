from rest_framework import serializers
from enderecosusuario.models import EnderecosUsuario

class EnderecosUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnderecosUsuario
        fields = '__all__'