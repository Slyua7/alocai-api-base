from rest_framework import generics
from agendamento.models import Agendamento
from agendamento.serializers import AgendamentoSerializer

class AgendamentoCreateListView(generics.ListCreateAPIView):
    queryset = Agendamento.objects.all()
    serializer_class = AgendamentoSerializer

class AgendamentoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Agendamento.objects.all()
    serializer_class = AgendamentoSerializer