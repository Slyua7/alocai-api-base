from django.db import models
from sala.models import Sala

class Auditorio(models.Model):
    sala = models.ForeignKey(Sala, on_delete=models.PROTECT, related_name='auditorio')
    capacidade_pessoas = models.IntegerField()

    def __str__(self):
        return self.sala