from django.db import models
from constructor.models import Profile, Fittings

from constructor.models import Constructor


# Create your models here.
class WindowsillCalc(models.Model):
    price_windowsill = models.FloatField(max_length=255, default=0.0)
    width = models.FloatField(max_length=255, default=0.0)
    length = models.FloatField(max_length=255, default=0.0)
    count = models.FloatField(max_length=255, default=0.0)
    # sum = models.FloatField(max_length=255, default=0)


# _______________________________ CALCULATION MODEL _______________________________
class WindowDiscount(models.Model):
    profile_id = models.ForeignKey(Profile, verbose_name="Профиль", blank=True, null=True, on_delete=models.CASCADE)
    fittings_id = models.ForeignKey(Fittings, verbose_name="фурнитура", blank=True, null=True, on_delete=models.CASCADE)
    discount = models.FloatField(max_length=255, default=0.0)

    def __str__(self):
        return f'Профиль : {self.profile_id.name} + Фурнитура: {self.fittings_id.name} = {self.discount} %'

    class Meta:
        verbose_name = 'Скидка на окно'
        verbose_name_plural = 'Скидки на окна'


class ExchangeRates(models.Model):
    name = models.CharField(max_length=255)
    value = models.FloatField(max_length=255, default=0.0)

    def __str__(self):
        return f'1 {self.name} = {self.value} BYN '

    class Meta:
        verbose_name = 'Курс валют'
        verbose_name_plural = 'Курсы валют'


class Order(models.Model):
    constructor_id = models.ForeignKey(Constructor, verbose_name="Конструктор", blank=True, null=True, on_delete=models.CASCADE)
