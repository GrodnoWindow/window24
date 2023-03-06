from django.db import models
from users.models import User
from client.models import Client
from users.models import User


class Windowsill(models.Model):
    UNIT = [
        {1, 'м2'},
        {2, 'шт'}
    ]
    name = models.CharField(max_length=255, blank=True, null=True, verbose_name='Название')
    price_in_currency = models.FloatField(blank=True, null=True, verbose_name=' Цена EUR/USD')
    price_in_byn = models.FloatField(blank=True, null=True, verbose_name='Цена BYN')
    unit = models.PositiveSmallIntegerField(("Единица измерения"), choices=UNIT, default=1)

    def __str__(self):
        return f' Название: {self.name} {self.price_in_currency} EUR/USD {self.price_in_byn} BYN'

    class Meta:
        verbose_name = 'Подоконник'
        verbose_name_plural = 'Подоконники'


class WindowsillCalc(models.Model):
    order_id = models.IntegerField(verbose_name='Номер замера', blank=True, null=True)
    windowsill = models.ForeignKey(Windowsill, models.SET_NULL, verbose_name='Подоконник', blank=True, null=True)
    width = models.IntegerField(default=0, verbose_name='Ширина')
    length = models.IntegerField(default=0, verbose_name='Длинна')
    count = models.IntegerField(default=0, verbose_name='Количество')
    square_meter = models.FloatField(max_length=255, default=0.0, verbose_name='В метрах квадратных')
    linear_meter = models.FloatField(max_length=255, default=0.0, verbose_name='В метрах погонных')
    price_in_byn = models.FloatField(max_length=255, default=0.0, verbose_name='Цена BYN')
    price_in_currency = models.FloatField(max_length=255, default=0.0, verbose_name='Цена EUR/USD')

    def __str__(self):
        return f' Номер замера {self.order_id} Подоконник {self.windowsill}  на сумму {self.price_in_byn} BYN'

    class Meta:
        verbose_name = 'Просчет подоконника'
        verbose_name_plural = 'Просчеты подоконников'


class WindowsillComplectCalc(models.Model):
    order_id = models.IntegerField(verbose_name='Номер замера', blank=True, null=True)
    windowsill = models.ForeignKey(Windowsill, models.SET_NULL, verbose_name='Комплектующие подоконника', blank=True,
                                   null=True)
    count = models.IntegerField(default=0, verbose_name='Количество')
    price_in_byn = models.FloatField(max_length=255, default=0.0, verbose_name='Цена BYN')
    price_in_currency = models.FloatField(max_length=255, default=0.0, verbose_name='Цена EUR/USD')

    def __str__(self):
        return f' Номер замера {self.order_id} Подоконник {self.windowsill}  на сумму {self.price_in_byn} BYN'

    class Meta:
        verbose_name = 'Просчет комплектующих подоконников'
        verbose_name_plural = 'Просчеты комплектующих подоконника'


class LowTides(models.Model):
    UNIT = [
        {1, 'м2'},
        {2, 'шт'}
    ]
    name = models.CharField(max_length=255, blank=True, null=True, verbose_name='Название')
    price_in_currency = models.FloatField(blank=True, null=True, verbose_name=' Цена EUR/USD')
    price_in_byn = models.FloatField(blank=True, null=True, verbose_name='Цена BYN')
    unit = models.PositiveSmallIntegerField(("Единица измерения"), choices=UNIT)

    def __str__(self):
        return f' Название: {self.name} {self.price_in_currency} EUR/USD {self.price_in_byn} BYN'

    class Meta:
        verbose_name = 'Отлив'
        verbose_name_plural = 'Отливы'


class LowTidesCalc(models.Model):
    order_id = models.IntegerField(verbose_name='Номер замера', blank=True, null=True)
    low_tides = models.ForeignKey(LowTides, models.SET_NULL, verbose_name='Отлив', blank=True, null=True)
    width = models.IntegerField(default=0, verbose_name='Ширина')
    length = models.IntegerField(default=0, verbose_name='Длинна')
    count = models.IntegerField(default=0, verbose_name='Количество')
    square_meter = models.FloatField(max_length=255, default=0.0, verbose_name='В метрах квадратных')
    linear_meter = models.FloatField(max_length=255, default=0.0, verbose_name='В метрах погонных')
    price_in_byn = models.FloatField(max_length=255, default=0.0, verbose_name='Цена BYN')
    price_in_currency = models.FloatField(max_length=255, default=0.0, verbose_name='Цена EUR/USD')

    def __str__(self):
        return f' Номер замера {self.order_id} Подоконник {self.low_tides}  на сумму {self.price_in_byn} BYN'

    class Meta:
        verbose_name = 'Просчет отлива'
        verbose_name_plural = 'Просчеты отливов'


class LowTidesComplectCalc(models.Model):
    order_id = models.IntegerField(verbose_name='Номер замера', blank=True, null=True)
    low_tides = models.ForeignKey(LowTides, models.SET_NULL, verbose_name='Комплектующие отлива', blank=True, null=True)
    count = models.IntegerField(default=0, verbose_name='Количество')
    price_in_byn = models.FloatField(max_length=255, default=0.0, verbose_name='Цена BYN')
    price_in_currency = models.FloatField(max_length=255, default=0.0, verbose_name='Цена EUR/USD')

    def __str__(self):
        return f' Номер замера {self.order_id} Подоконник {self.low_tides}  на сумму {self.price_in_byn} BYN'

    class Meta:
        verbose_name = 'Просчет комплектующих отливов'
        verbose_name_plural = 'Просчеты комплектующих отливов'


class Status(models.Model):
    name = models.CharField(max_length=100, verbose_name='Статус', blank=True, null=True)

    def __str__(self):
        return f' № {self.pk} {self.name}'

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'


class Order(models.Model):
    STATUS = [
        {0, 'Активная заявка'},
        {1, 'Договор заключен'},
        {2, 'Думает'},
        {3, 'Придет на офис'},
        {4, 'Банковская рассрочка'},
        {5, 'Отказ до замера'},
        {6, 'Отказ после замера'}
    ]
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name='Замерщик')
    address = models.CharField(max_length=255, blank=True, null=True, verbose_name='Адрес')
    name = models.CharField(max_length=255, blank=True, null=True, verbose_name='Имя заказчика')
    phone = models.CharField(max_length=255, blank=True, null=True, verbose_name='Номер телефона')
    date = models.DateField(verbose_name='Дата замера')
    sum_in_byn = models.FloatField(default=0.0, verbose_name='Сумма просчета BYN')
    sum_in_currency = models.FloatField(default=0.0, verbose_name='Сумма просчета в EUR/USD')
    status = models.ForeignKey(Status, on_delete=models.SET_NULL, verbose_name='статус', null=True, blank=True)
    windowsill_calc = models.ManyToManyField(WindowsillCalc, blank=True, verbose_name='Просчеты подоконников')

    class Meta:
        verbose_name = 'Замер'
        verbose_name_plural = 'Замеры'

    def __str__(self):
        return f' Адрес: {self.address} Cтатус: {self.status} Сумма {self.sum_in_byn} BYN Сумма {self.sum_in_currency} EUR/USD'
