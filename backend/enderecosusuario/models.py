from django.db import models
from django.core.validators import RegexValidator

VALIDACAO_CEP = RegexValidator(
        regex=r'^\d{5}-?\d{3}$',
        message="CEP inválido. O formato deve ser 12345-678 ou 12345678."
    )

class EnderecosUsuario(models.Model):
    cep = models.CharField(max_length=9, validators=[VALIDACAO_CEP])
    rua = models.CharField(max_length=40)
    numero = models.CharField(max_length=6, null=True, blank=True)

    def __str__(self):
        return self.rua