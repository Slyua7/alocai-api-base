from rest_framework import serializers
from auditorio.models import Auditorio

class AuditorioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Auditorio
        fields = '__all__'