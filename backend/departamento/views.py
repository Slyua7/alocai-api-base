from rest_framework import generics
from departamento.models import Departamento
from departamento.serializers import DepartamentoSerializer

class DepartamentoCreateListView(generics.ListCreateAPIView):
    queryset = Departamento.objects.all()
    serializer_class = DepartamentoSerializer

class DepartamentoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Departamento.objects.all()
    serializer_class = DepartamentoSerializer