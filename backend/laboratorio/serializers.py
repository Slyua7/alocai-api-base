from rest_framework import serializers
from laboratorio.models import Laboratorio

class LaboratorioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Laboratorio
        fields = '__all__'