from rest_framework import serializers
from sala.models import Sala

class SalaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sala
        fields = '__all__'