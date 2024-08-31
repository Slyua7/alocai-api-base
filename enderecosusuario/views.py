from rest_framework import generics
from enderecosusuario.models import EnderecosUsuario
from enderecosusuario.serializers import EnderecosUsuarioSerializer

class EnderecosUsuarioCreateListView(generics.ListCreateAPIView):
    queryset = EnderecosUsuario.objects.all()
    serializer_class = EnderecosUsuarioSerializer

class EnderecosUsuarioRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = EnderecosUsuario.objects.all()
    serializer_class = EnderecosUsuarioSerializer