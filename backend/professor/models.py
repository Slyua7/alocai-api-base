from django.db import models
from django.contrib.auth.models import User

class Professor(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT, related_name='professor')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"