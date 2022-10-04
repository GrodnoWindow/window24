from django.db import models


from call.models import Call


class Number(models.Model):
    number = models.CharField(max_length=255,blank=True)

    def __str__(self):
        return self.number


class Client(models.Model):
    author = models.CharField(max_length=255, blank=True)
    name = models.CharField(max_length=255, blank=True)
    numbers = models.ManyToManyField(Number, null=True, blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    calls = models.ManyToManyField(Call, null=True, blank=True)

    def __str__(self):
        return self.name
