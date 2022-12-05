from django.db import models

from call.models import Call
from miscalculation.models import Miscalculation


class Number(models.Model):
    number = models.CharField(max_length=255, blank=True)
    name = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.number


class Address(models.Model):
    name = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name


class Client(models.Model):
    author = models.CharField(max_length=255, blank=True)
    name = models.CharField(max_length=255, blank=True)
    numbers = models.ManyToManyField(Number, blank=True)
    addresses = models.ManyToManyField(Address, blank=True)
    time_created = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    calls = models.ManyToManyField(Call, blank=True)
    miscalculation = models.ManyToManyField(Miscalculation, verbose_name="Просчеты", blank=True)

    def __str__(self):
        return self.name
