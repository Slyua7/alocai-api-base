from django.db import models
from sala.models import Sala

class Auditorio(models.Model):
    sala_auditorio = models.ForeignKey(Sala, on_delete=models.PROTECT, related_name='auditorios')
    capacidade_pessoas = models.IntegerField()

    def __str__(self):
        return self.sala_auditorio