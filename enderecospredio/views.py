from rest_framework import generics
from enderecospredio.models import EnderecosPredio
from enderecospredio.serializers import EnderecosPredioSerializer

class EnderecosPredioCreateListView(generics.ListCreateAPIView):
    queryset = EnderecosPredio.objects.all()
    serializer_class = EnderecosPredioSerializer

class EnderecosPredioRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = EnderecosPredio.objects.all()
    serializer_class = EnderecosPredioSerializer