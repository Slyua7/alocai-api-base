from rest_framework import generics
from sala.models import Sala
from sala.serializers import SalaSerializer

class SalaCreateListView(generics.ListCreateAPIView):
    queryset = Sala.objects.all()
    serializer_class = SalaSerializer

class SalaRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sala.objects.all()
    serializer_class = SalaSerializer