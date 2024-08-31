from django.db import models
from django.contrib.auth.models import User

class Coordenador(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT, related_name='coordenador')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"