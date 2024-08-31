from django.db import models
from departamento.models import Departamento
from predio.models import Predio

class PredioDep(models.Model):
    id_dep = models.ForeignKey(Departamento, on_delete=models.PROTECT, related_name='predio_dep')
    id_predio = models.ForeignKey(Predio, on_delete=models.PROTECT, related_name='predio_dep')