from rest_framework import generics
from sala_desenho.models import SalaDesenho
from sala_desenho.serializers import SalaDesenhoSerializer

class SalaDesenhoCreateListView(generics.ListCreateAPIView):
    queryset = SalaDesenho.objects.all()
    serializer_class = SalaDesenhoSerializer

class SalaDesenhoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SalaDesenho.objects.all()
    serializer_class = SalaDesenhoSerializer