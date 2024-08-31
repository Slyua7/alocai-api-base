from rest_framework import serializers
from sala_desenho.models import SalaDesenho

class SalaDesenhoSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalaDesenho
        fields = '__all__'