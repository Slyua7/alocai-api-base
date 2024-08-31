from django.db import models
from enderecosusuario.models import EnderecosUsuario
from django.contrib.auth.models import User

TIPO_USUARIO = (
        ('aluno', 'Aluno'),
        ('professor', 'Professor'),
    )

class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT, related_name='usuario')
    nascimento = models.DateField()
    id_endereco_usuario = models.ForeignKey(EnderecosUsuario, on_delete=models.PROTECT, related_name='usuario')
    tipo = models.CharField(max_length=10, choices=TIPO_USUARIO)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} ({self.tipo})"