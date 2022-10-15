from django.db import models
from constructor.models import Profile, Fittings, Windowsill, LowTides


class Markups(models.Model):
    windowsill = models.FloatField(default=0.0, max_length=255, verbose_name='Подоконники в %')
    low_tides = models.FloatField(default=0.0, max_length=255, verbose_name='Отливы в %')

    def __str__(self):
        return f' Наценки № {self.id}'

    class Meta:
        verbose_name = 'Наценки'
        verbose_name_plural = 'Наценки'


# _______________________________ CALCULATION Windowsill/LowTides MODEL _______________________________
class LowTidesCalc(models.Model):
    low_tides = models.ForeignKey(LowTides, verbose_name="Отлив", blank=True, null=True,
                                  on_delete=models.CASCADE)
    width = models.FloatField(max_length=255, default=0.0)
    length = models.FloatField(max_length=255, default=0.0)
    count = models.FloatField(max_length=255, default=0.0)
    price_output = models.FloatField(max_length=255, default=0.0)

    def __str__(self):
        return f' Отлив № {self.id} : {self.low_tides.name} {self.low_tides.type} = {self.price_output} BYN'

    class Meta:
        verbose_name = 'Просчет подоконника'
        verbose_name_plural = 'Просчеты подоконников'


class WindowsillCalc(models.Model):
    windowsill = models.ForeignKey(Windowsill, verbose_name="Подоконник", blank=True, null=True,
                                   on_delete=models.CASCADE)
    width = models.FloatField(max_length=255, default=0.0)
    length = models.FloatField(max_length=255, default=0.0)
    count = models.FloatField(max_length=255, default=0.0)
    price_output = models.FloatField(max_length=255, default=0.0)

    def __str__(self):
        return f' Подоконник № {self.id} : {self.windowsill.color} {self.windowsill.type} = {self.price_output} BYN'

    class Meta:
        verbose_name = 'Просчет подоконника'
        verbose_name_plural = 'Просчеты подоконников'


# _______________________________ CALCULATION MODEL _______________________________
class WindowDiscount(models.Model):
    profile_id = models.ForeignKey(Profile, verbose_name="Профиль", blank=True, null=True, on_delete=models.CASCADE)
    fitting_id = models.ForeignKey(Fittings, verbose_name="Фурнитура", blank=True, null=True, on_delete=models.CASCADE)
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
