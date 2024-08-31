from rest_framework import serializers
from enderecospredio.models import EnderecosPredio

class EnderecosPredioSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnderecosPredio
        fields = '__all__'