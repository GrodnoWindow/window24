from django.db import models
from client.models import Client


class Call(models.Model):
    from_phone = models.CharField(max_length=255)
    to_phone = models.CharField(max_length=255)
    datetime = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True, blank=True)
    comment = models.CharField(max_length=255)
    manager = models.CharField(max_length=255)


    def __str__(self):
        return self.from_phone


