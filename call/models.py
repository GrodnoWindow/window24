from django.db import models
from client.models import Client


class Call(models.Model):
    date = models.DateField()
    time = models.TimeField()
    from_phone = models.CharField(max_length=255)
    to_phone = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True, verbose_name='Клиент', blank=True)

    manager = models.CharField(max_length=255)


    def __str__(self):
        return self.from_phone

