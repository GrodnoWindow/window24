from django.db import models
from client.models import Client
from users.models import User


class Calculations(models.Model):
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True, blank=True)
    # окна просчет
    datetime = models.CharField(max_length=255)
    sum = models.CharField(max_length=255)
    manager = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    status = models.CharField(max_length=255)