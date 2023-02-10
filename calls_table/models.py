from django.db import models
from client.models import Client
from call.models import Call


# Create your models here.
class CallsTable(models.Model):
    call = models.ForeignKey(Call, on_delete=models.CASCADE, blank=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return f'{self.pk} {self.client.name}'


