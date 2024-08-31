from django.db import models
from sala.models import Sala

class Laboratorio(models.Model):
    sala_laboratorio = models.ForeignKey(Sala, on_delete=models.PROTECT, related_name='laboratorios')
    qtd_maquinas = models.IntegerField()
    softwares = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return self.sala_laboratorio