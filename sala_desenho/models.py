from django.db import models
from sala.models import Sala

class SalaDesenho(models.Model):
    sala = models.ForeignKey(Sala, on_delete=models.PROTECT, related_name='sala_desenho')
    qtd_cadeiras_desenho = models.IntegerField()
    materiais_disponiveis = models.CharField(max_length=100)

    def __str__(self):
        return self.sala