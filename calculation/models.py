from django.db import models
from constructor.models import Profile, Fittings, Windowsill, LowTides


class Markups(models.Model):
    windowsill = models.FloatField(default=0.0, max_length=255, verbose_name='Подоконники в %')
    low_tides = models.FloatField(default=0.0, max_length=255, verbose_name='Отливы в %')
    window = models.FloatField(default=0.0, max_length=255, verbose_name='Окна в %')

    def __str__(self):
        return f' Наценки № {self.id}'

    class Meta:
        verbose_name = 'Наценки'
        verbose_name_plural = 'Наценки'


# _______________________________ CALCULATION MODELS _______________________________
class LowTidesCalc(models.Model):
    low_tides_id = models.IntegerField(default=0.0, verbose_name="№ Отлив", blank=True, null=True)

    width = models.FloatField(max_length=255, default=0.0, verbose_name='ширина')
    length = models.FloatField(max_length=255, default=0.0, verbose_name='длинна')
    count = models.FloatField(max_length=255, default=0.0, verbose_name='количество')
    price_output = models.FloatField(max_length=255, default=0.0,verbose_name='цена')

    def __str__(self):
        return f' Отлив № {self.id} длинна {self.length} / ширина {self.width} = {self.price_output} BYN'

    class Meta:
        verbose_name = 'Просчет отлива'
        verbose_name_plural = 'Просчеты отливов'


class WindowsillCalc(models.Model):
    windowsill_id = models.IntegerField(default=0.0, verbose_name="№ Подоконник", blank=True, null=True)
    width = models.FloatField(max_length=255, default=0.0, verbose_name='ширина')
    length = models.FloatField(max_length=255, default=0.0, verbose_name='длинна')
    count = models.FloatField(max_length=255, default=0.0, verbose_name='количество')
    price_output = models.FloatField(max_length=255, default=0.0, verbose_name='цена')

    def __str__(self):
        return f' Подоконник № {self.id}  на сумму {self.price_output} BYN'

    class Meta:
        verbose_name = 'Просчет подоконника'
        verbose_name_plural = 'Просчеты подоконников'


class WindowDiscount(models.Model):
    profile_id = models.ForeignKey(Profile, verbose_name="Профиль", blank=True, null=True, on_delete=models.CASCADE)
    fittings_id = models.ForeignKey(Fittings, verbose_name="Фурнитура", blank=True, null=True, on_delete=models.CASCADE)
    value = models.FloatField(max_length=255, default=0.0, verbose_name='Значение')

    def __str__(self):
        return f'Профиль : {self.profile_id.name} + Фурнитура: {self.fittings_id.name} = {self.value} %'

    class Meta:
        verbose_name = 'Скидка на окно'
        verbose_name_plural = 'Скидки на окна'


class ExchangeRates(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя')
    value = models.FloatField(max_length=255, default=0.0, verbose_name='Значение')

    def __str__(self):
        return f'1 {self.name} = {self.value} BYN '

    class Meta:
        verbose_name = 'Курс валют'
        verbose_name_plural = 'Курсы валют'


class WindowsCalc(models.Model):
    discount = models.FloatField(max_length=255, verbose_name="Скидка на окно", blank=True, null=True)
    currency_name = models.CharField(max_length=255, verbose_name='Валюта имя',blank=True,null=True)
    currency_value = models.FloatField(max_length=255, verbose_name='Валюта значение НБРБ',blank=True,null=True)
    price_input = models.FloatField(max_length=255, default=0.0, verbose_name='Входная цена')
    price_output = models.FloatField(max_length=255, default=0.0, verbose_name='Выходная цена ( с наценкой )')

    def __str__(self):
        return f' Просчет окна № {self.id} на сумму {self.price_output} BYN'

    class Meta:
        verbose_name = 'Просчет окна'
        verbose_name_plural = 'Просчеты окон'
