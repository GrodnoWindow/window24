from django.db import models
from client.models import Client


class Calculations(models.Model):
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True, blank=True)
    # окна просчет
    timestamp = models.CharField(max_length=255)
    sum = models.CharField(max_length=255)
    manager = models.CharField(max_length=255)
    status = models.CharField(max_length=255)