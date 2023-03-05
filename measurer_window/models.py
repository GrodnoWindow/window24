from django.db import models
from users.models import User
from client.models import Client
from users.models import User




class Windowsill(models.Model):
    UNIT = [
        {1, 'шт'},
        {2, 'м2'}
    ]
    name = models.CharField(max_length=255, blank=True, null=True, verbose_name='Название')
    price_in_currency = models.FloatField(blank=True, null=True, verbose_name=' Цена EUR/USD')
    price = models.FloatField(blank=True, null=True, verbose_name='Цена BYN')
    unit = models.PositiveSmallIntegerField(("Единица измерения"), choices=UNIT)

    def __str__(self):
        return f' Название: {self.name} {self.price_in_currency} EUR/USD {self.price} BYN'

    class Meta:
        verbose_name = 'Подоконник'
        verbose_name_plural = 'Подоконники'


class WindowsillCalc(models.Model):
    windowsill = models.ForeignKey(Windowsill, models.SET_NULL, verbose_name='Подоконник', blank=True, null=True)
    width = models.FloatField(max_length=255, default=0.0, verbose_name='Ширина')
    length = models.FloatField(max_length=255, default=0.0, verbose_name='Длинна')
    count = models.FloatField(max_length=255, default=0.0, verbose_name='Количество')
    square_meter = models.FloatField(max_length=255, default=0.0, verbose_name='В метрах квадратных')
    linear_meter = models.FloatField(max_length=255, default=0.0, verbose_name='В метрах погонных')
    price_output = models.FloatField(max_length=255, default=0.0, verbose_name='Цена')

    def __str__(self):
        return f' Подоконник № {self.windowsill}  на сумму {self.price_output} BYN'

    class Meta:
        verbose_name = 'Просчет подоконника'
        verbose_name_plural = 'Просчеты подоконников'

class Order(models.Model):
    STATUS = [
        {1, 'Заключен договор'},
        {2, 'Отказ после замера'},
        {3, 'Придет на офис'}
    ]
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=255, blank=True, null=True, verbose_name='Адрес')
    name = models.CharField(max_length=255, blank=True, null=True, verbose_name='Имя заказчика')
    phone = models.CharField(max_length=255, blank=True, null=True, verbose_name='Номер телефона')
    date = models.DateField(verbose_name='Дата замера')
    sum = models.FloatField(default=0.0, verbose_name='Сумма просчета')
    sum_in_currency = models.FloatField(default=0.0, verbose_name='Сумма просчета в EUR/USD')
    status = models.PositiveSmallIntegerField(("Статус"), choices=STATUS, blank=True, null=True)
    windowsill_calc = models.ManyToManyField(WindowsillCalc,)
    class Meta:
        verbose_name = 'Замер'
        verbose_name_plural = 'Замеры'

    def __str__(self):
        return f' Адрес: {self.address} Cтатус: {self.status} Сумма {self.sum} BYN Сумма {self.sum_in_currency} EUR/USD'
