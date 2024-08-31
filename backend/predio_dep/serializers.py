from rest_framework import serializers
from predio_dep.models import PredioDep

class PredioDepSerializer(serializers.ModelSerializer):
    class Meta:
        model = PredioDep
        fields = '__all__'