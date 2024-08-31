from rest_framework import generics
from auditorio.models import Auditorio
from auditorio.serializers import AuditorioSerializer

class AuditorioCreateListView(generics.ListCreateAPIView):
    queryset = Auditorio.objects.all()
    serializer_class = AuditorioSerializer

class AuditorioRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Auditorio.objects.all()
    serializer_class = AuditorioSerializer