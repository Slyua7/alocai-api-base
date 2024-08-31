from django.db import models
from coordenador.models import Coordenador

class Departamento(models.Model):
    nome = models.CharField(max_length=30)
    universidade = models.CharField(max_length=10)
    area = models.CharField(max_length=60)
    id_coordenador = models.ForeignKey(Coordenador, on_delete=models.PROTECT, related_name='departamento')

    def __str__(self):
        return self.nome