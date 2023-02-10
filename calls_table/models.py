from django.db import models
from client.models import Client
from call.models import Call


# Create your models here.
class CallsTable(models.Model):
    call = models.ForeignKey(Call, on_delete=models.CASCADE, blank=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return f'{self.pk} {self.client.name}'


class OutgoingCalls(models.Model):
    phone = models.CharField(max_length=255, blank=True,null=True)
    datetime = models.DateTimeField(auto_now_add=True)
    number = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f'{self.pk} {self.phone} {self.datetime} с телефона {self.number}'