from rest_framework import generics
from coordenador.models import Coordenador
from coordenador.serializers import CoordenadorSerializer

class CoordenadorCreateListView(generics.ListCreateAPIView):
    queryset = Coordenador.objects.all()
    serializer_class = CoordenadorSerializer

class CoordenadorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Coordenador.objects.all()
    serializer_class = CoordenadorSerializer