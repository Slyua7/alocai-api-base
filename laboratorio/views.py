from rest_framework import generics
from laboratorio.models import Laboratorio
from laboratorio.serializers import LaboratorioSerializer

class LaboratorioCreateListView(generics.ListCreateAPIView):
    queryset = Laboratorio.objects.all()
    serializer_class = LaboratorioSerializer

class LaboratorioRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Laboratorio.objects.all()
    serializer_class = LaboratorioSerializer