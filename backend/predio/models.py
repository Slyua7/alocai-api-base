from django.db import models
from enderecospredio.models import EnderecosPredio

class Predio(models.Model):
    nome = models.CharField(max_length=40)
    id_endereco_predio = models.ForeignKey(EnderecosPredio, on_delete=models.PROTECT, related_name='predio')

    def __str__(self):
        return self.nome