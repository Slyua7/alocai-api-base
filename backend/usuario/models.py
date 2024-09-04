from django.db import models
from django.contrib.auth.models import User

TIPO_USUARIO = (
        ('aluno', 'Aluno'),
        ('professor', 'Professor'),
    )

class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT, related_name='usuario')
    nascimento = models.DateField()
    tipo = models.CharField(max_length=10, choices=TIPO_USUARIO)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} ({self.tipo})"