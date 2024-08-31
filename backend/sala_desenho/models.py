from django.db import models
from sala.models import Sala

class SalaDesenho(models.Model):
    sala_desenho = models.ForeignKey(Sala, on_delete=models.PROTECT, related_name='sala_desenhos')
    qtd_cadeiras_desenho = models.IntegerField()
    materiais_disponiveis = models.CharField(max_length=100)

    def __str__(self):
        return self.sala_desenho