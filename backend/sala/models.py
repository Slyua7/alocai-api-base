from django.db import models
from predio.models import Predio

class Sala(models.Model):
    numero = models.IntegerField()
    descricao = models.CharField(max_length=100)
    qtd_cadeiras = models.IntegerField()
    andar = models.IntegerField()
    id_predio = models.ForeignKey(Predio, on_delete=models.PROTECT, related_name='sala')

    def __str__(self):
        return f"{self.id_predio.nome} / {self.andar} / {self.numero}"