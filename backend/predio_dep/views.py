from rest_framework import generics
from predio_dep.models import PredioDep
from predio_dep.serializers import PredioDepSerializer

class PredioDepCreateListView(generics.ListCreateAPIView):
    queryset = PredioDep.objects.all()
    serializer_class = PredioDepSerializer

class PredioDepRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PredioDep.objects.all()
    serializer_class = PredioDepSerializer