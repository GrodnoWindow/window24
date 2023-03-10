from django.db import models
from users.models import User
from client.models import Client
from users.models import User


class Status(models.Model):
    name = models.CharField(max_length=100, verbose_name='Статус', blank=True, null=True)

    def __str__(self):
        return f' № {self.pk} {self.name}'

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'


class Unit(models.Model):
    name = models.CharField(max_length=100, verbose_name='Единица измерия', blank=True, null=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Единица измерения'
        verbose_name_plural = 'Единица измерения'


class WindowsillWidth(models.Model):
    name = models.CharField(max_length=100, verbose_name='Полка подоконника', blank=True, null=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Полка подоконника'
        verbose_name_plural = 'Полки подоконников'


class WindowsillColor(models.Model):
    name = models.CharField(max_length=100, verbose_name='Цвет подоконника', blank=True, null=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Цвет подоконника'
        verbose_name_plural = 'Цвета подоконников'


class Windowsill(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True, verbose_name='Название')
    price_in_currency = models.FloatField(blank=True, null=True, verbose_name=' Цена EUR/USD')
    price_in_byn = models.FloatField(blank=True, null=True, verbose_name='Цена BYN')
    unit = models.ForeignKey(Unit, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Единица измерения')

    def __str__(self):
        return f' Название: {self.name} {self.price_in_currency} EUR/USD {self.price_in_byn} BYN'

    class Meta:
        verbose_name = 'Подоконник'
        verbose_name_plural = 'Подоконники'


class WindowsillPlug(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True, verbose_name='Название')
    price_in_currency = models.FloatField(blank=True, null=True, verbose_name=' Цена EUR/USD')
    price_in_byn = models.FloatField(blank=True, null=True, verbose_name='Цена BYN')

    def __str__(self):
        return f' Название: {self.name} {self.price_in_currency} EUR/USD {self.price_in_byn} BYN'

    class Meta:
        verbose_name = 'Заглушка подоконника'
        verbose_name_plural = 'Заглушки подоконников'


class WindowsillConnection(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True, verbose_name='Название')
    price_in_currency = models.FloatField(blank=True, null=True, verbose_name=' Цена EUR/USD')
    price_in_byn = models.FloatField(blank=True, null=True, verbose_name='Цена BYN')

    def __str__(self):
        return f' Название: {self.name} {self.price_in_currency} EUR/USD {self.price_in_byn} BYN'

    class Meta:
        verbose_name = 'Соединитель подоконника'
        verbose_name_plural = 'Соединители подоконников'


class WindowsillCalc(models.Model):
    order_id = models.IntegerField(verbose_name='Номер замера', blank=True, null=True)
    windowsill = models.ForeignKey(Windowsill, models.SET_NULL, verbose_name='Подоконник', blank=True, null=True)
    windowsill_width = models.ForeignKey(WindowsillWidth, models.SET_NULL, verbose_name='Полка подоконник', blank=True,
                                         null=True)

    length = models.IntegerField(default=0, verbose_name='Длинна')
    windowsill_color = models.ForeignKey(WindowsillColor, models.SET_NULL, verbose_name='Цвет подоконника', blank=True,
                                         null=True)
    windowsill_count = models.IntegerField(default=0, verbose_name='Количество  подоконников')

    windowsill_plug = models.ForeignKey(WindowsillPlug, models.SET_NULL, verbose_name='Заглушка подоконника',
                                        blank=True,
                                        null=True)
    windowsill_plug_count = models.IntegerField(default=0, blank=True, null=True, verbose_name='Количество заглушек')
    windowsill_connection = models.ForeignKey(WindowsillConnection, models.SET_NULL,
                                              verbose_name='Соединитель подоконника', blank=True,
                                              null=True)
    windowsill_connection_count = models.IntegerField(default=0, blank=True, null=True,
                                                      verbose_name='Количество соединителей')

    square_meter = models.FloatField(max_length=255, default=0.0, verbose_name='В метрах квадратных', blank=True, null=True)
    linear_meter = models.FloatField(max_length=255, default=0.0, verbose_name='В метрах погонных', blank=True, null=True)

    sum_plug_byn = models.FloatField(max_length=255, default=0.0, verbose_name='Цена заглушек в BYN', blank=True, null=True)
    sum_plug_currency = models.FloatField(max_length=255, default=0.0, verbose_name='Цена заглушек в EUR/USD', blank=True, null=True)

    sum_connection_byn = models.FloatField(max_length=255, default=0.0, verbose_name='Цена соединитеей в BYN', blank=True, null=True)
    sum_connection_currency = models.FloatField(max_length=255, default=0.0, verbose_name='Цена соединителей в EUR/USD', blank=True, null=True)

    sum_windowsill_byn = models.FloatField(max_length=255, default=0.0, verbose_name='Цена подоконника в BYN', blank=True, null=True)
    sum_windowsill_currency = models.FloatField(max_length=255, default=0.0, verbose_name='Цена подоконника в EUR/USD', blank=True, null=True)

    sum_in_byn = models.FloatField(max_length=255, default=0.0, verbose_name='Цена BYN', blank=True, null=True)
    sum_in_currency = models.FloatField(max_length=255, default=0.0, verbose_name='Цена EUR/USD', blank=True, null=True)

    def __str__(self):
        return f' Номер замера {self.order_id} Подоконник {self.windowsill}  на сумму {self.sum_in_byn} BYN'

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
        return f' Номер замера {self.order_id} комплектующие подоконника {self.windowsill}  на сумму {self.price_in_byn} BYN'

    class Meta:
        verbose_name = 'Просчет комплектующих подоконников'
        verbose_name_plural = 'Просчеты комплектующих подоконника'


class LowTides(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True, verbose_name='Название')
    price_in_currency = models.FloatField(blank=True, null=True, verbose_name=' Цена EUR/USD')
    price_in_byn = models.FloatField(blank=True, null=True, verbose_name='Цена BYN')
    unit = models.ForeignKey(Unit, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Единица измерения')

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
        return f' Номер замера {self.order_id} отлив {self.low_tides}  на сумму {self.price_in_byn} BYN'

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
        return f' Номер замера {self.order_id} комплектующие отлива {self.low_tides}  на сумму {self.price_in_byn} BYN'

    class Meta:
        verbose_name = 'Просчет комплектующих отливов'
        verbose_name_plural = 'Просчеты комплектующих отливов'


class Visors(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True, verbose_name='Название')
    price_in_currency = models.FloatField(blank=True, null=True, verbose_name='Цена EUR/USD')
    price_in_byn = models.FloatField(blank=True, null=True, verbose_name='Цена BYN')

    def __str__(self):
        return f' Название: {self.name} {self.price_in_currency} EUR/USD {self.price_in_byn} BYN'

    class Meta:
        verbose_name = 'Козырек'
        verbose_name_plural = 'козырьки'


class VisorsCalc(models.Model):
    order_id = models.IntegerField(verbose_name='Номер замера', blank=True, null=True)
    visors = models.ForeignKey(Visors, models.SET_NULL, verbose_name='Козырек', blank=True, null=True)
    width = models.IntegerField(default=0, verbose_name='Ширина')
    length = models.IntegerField(default=0, verbose_name='Длинна')
    count = models.IntegerField(default=0, verbose_name='Количество')
    square_meter = models.FloatField(max_length=255, default=0.0, verbose_name='В метрах квадратных')
    linear_meter = models.FloatField(max_length=255, default=0.0, verbose_name='В метрах погонных')
    price_in_byn = models.FloatField(max_length=255, default=0.0, verbose_name='Цена BYN')
    price_in_currency = models.FloatField(max_length=255, default=0.0, verbose_name='Цена EUR/USD')

    def __str__(self):
        return f' Номер замера {self.order_id} козырек {self.visors}  на сумму {self.price_in_byn} BYN'

    class Meta:
        verbose_name = 'Просчет козырька'
        verbose_name_plural = 'Просчеты козырьков'


class Flashing(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True, verbose_name='Название')
    price_in_currency = models.FloatField(blank=True, null=True, verbose_name='Цена EUR/USD')
    price_in_byn = models.FloatField(blank=True, null=True, verbose_name='Цена BYN')

    def __str__(self):
        return f' Название: {self.name} {self.price_in_currency} EUR/USD {self.price_in_byn} BYN'

    class Meta:
        verbose_name = 'Нащельник'
        verbose_name_plural = 'Нащельники'


class FlashingCalc(models.Model):
    order_id = models.IntegerField(verbose_name='Номер замера', blank=True, null=True)
    flashing = models.ForeignKey(Flashing, models.SET_NULL, verbose_name='Нащельник', blank=True, null=True)
    width = models.IntegerField(default=0, verbose_name='Ширина')
    length = models.IntegerField(default=0, verbose_name='Длинна')
    count = models.IntegerField(default=0, verbose_name='Количество')
    square_meter = models.FloatField(max_length=255, default=0.0, verbose_name='В метрах квадратных')
    linear_meter = models.FloatField(max_length=255, default=0.0, verbose_name='В метрах погонных')
    price_in_byn = models.FloatField(max_length=255, default=0.0, verbose_name='Цена BYN')
    price_in_currency = models.FloatField(max_length=255, default=0.0, verbose_name='Цена EUR/USD')

    def __str__(self):
        return f' Номер замера {self.order_id} Нащельник {self.flashing}  на сумму {self.price_in_byn} BYN'

    class Meta:
        verbose_name = 'Просчет нащельника'
        verbose_name_plural = 'Просчеты нащельников'


class Casing(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True, verbose_name='Название')
    price_in_currency = models.FloatField(blank=True, null=True, verbose_name='Цена EUR/USD')
    price_in_byn = models.FloatField(blank=True, null=True, verbose_name='Цена BYN')

    def __str__(self):
        return f' Название: {self.name} {self.price_in_currency} EUR/USD {self.price_in_byn} BYN'

    class Meta:
        verbose_name = 'Наличник'
        verbose_name_plural = 'наличники'


class CasingCalc(models.Model):
    order_id = models.IntegerField(verbose_name='Номер замера', blank=True, null=True)
    casing = models.ForeignKey(Casing, models.SET_NULL, verbose_name='Наличник', blank=True, null=True)
    width = models.IntegerField(default=0, verbose_name='Ширина')
    length = models.IntegerField(default=0, verbose_name='Длинна')
    count = models.IntegerField(default=0, verbose_name='Количество')
    square_meter = models.FloatField(max_length=255, default=0.0, verbose_name='В метрах квадратных')
    linear_meter = models.FloatField(max_length=255, default=0.0, verbose_name='В метрах погонных')
    price_in_byn = models.FloatField(max_length=255, default=0.0, verbose_name='Цена BYN')
    price_in_currency = models.FloatField(max_length=255, default=0.0, verbose_name='Цена EUR/USD')

    def __str__(self):
        return f' Номер замера {self.order_id} наличник {self.casing}  на сумму {self.price_in_byn} BYN'

    class Meta:
        verbose_name = 'Просчет наличника'
        verbose_name_plural = 'Просчеты наличников'


class SlopesOfMetal(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True, verbose_name='Название')
    price_in_currency = models.FloatField(blank=True, null=True, verbose_name='Цена EUR/USD')
    price_in_byn = models.FloatField(blank=True, null=True, verbose_name='Цена BYN')

    def __str__(self):
        return f' Название: {self.name} {self.price_in_currency} EUR/USD {self.price_in_byn} BYN'

    class Meta:
        verbose_name = 'Откосы из металла'
        verbose_name_plural = 'Откосы из металла'


class SlopesOfMetalCalc(models.Model):
    order_id = models.IntegerField(verbose_name='Номер замера', blank=True, null=True)
    slopes_of_metal = models.ForeignKey(SlopesOfMetal, models.SET_NULL, verbose_name='Откосы из металла', blank=True,
                                        null=True)
    width = models.IntegerField(default=0, verbose_name='Ширина')
    length = models.IntegerField(default=0, verbose_name='Длинна')
    count = models.IntegerField(default=0, verbose_name='Количество')
    square_meter = models.FloatField(max_length=255, default=0.0, verbose_name='В метрах квадратных')
    linear_meter = models.FloatField(max_length=255, default=0.0, verbose_name='В метрах погонных')
    price_in_byn = models.FloatField(max_length=255, default=0.0, verbose_name='Цена BYN')
    price_in_currency = models.FloatField(max_length=255, default=0.0, verbose_name='Цена EUR/USD')

    def __str__(self):
        return f' Номер замера {self.order_id} Откос из металла {self.slopes_of_metal}  на сумму {self.price_in_byn} BYN'

    class Meta:
        verbose_name = 'Просчет откосов из металла'
        verbose_name_plural = 'Просчеты откосов из металла'


class InternalSlopes(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True, verbose_name='Название')
    price_in_currency = models.FloatField(blank=True, null=True, verbose_name='Цена EUR/USD')
    price_in_byn = models.FloatField(blank=True, null=True, verbose_name='Цена BYN')

    def __str__(self):
        return f' Название: {self.name} {self.price_in_currency} EUR/USD {self.price_in_byn} BYN'

    class Meta:
        verbose_name = 'Внутренние откосы'
        verbose_name_plural = 'Внутренние откосы'


class InternalSlopesCalc(models.Model):
    order_id = models.IntegerField(verbose_name='Номер замера', blank=True, null=True)
    internal_slopes = models.ForeignKey(InternalSlopes, models.SET_NULL, verbose_name='Внутренние откосы', blank=True,
                                        null=True)
    width = models.IntegerField(default=0, verbose_name='Ширина')
    length = models.IntegerField(default=0, verbose_name='Длинна')
    count = models.IntegerField(default=0, verbose_name='Количество')
    square_meter = models.FloatField(max_length=255, default=0.0, verbose_name='В метрах квадратных')
    linear_meter = models.FloatField(max_length=255, default=0.0, verbose_name='В метрах погонных')
    price_in_byn = models.FloatField(max_length=255, default=0.0, verbose_name='Цена BYN')
    price_in_currency = models.FloatField(max_length=255, default=0.0, verbose_name='Цена EUR/USD')

    def __str__(self):
        return f' Номер замера {self.order_id} внутренний откос {self.internal_slopes}  на сумму {self.price_in_byn} BYN'

    class Meta:
        verbose_name = 'Просчет внутренних откосов'
        verbose_name_plural = 'Просчеты внутренних откосов'


class MountingMaterials(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True, verbose_name='Название')
    price_in_currency = models.FloatField(blank=True, null=True, verbose_name='Цена EUR/USD')
    price_in_byn = models.FloatField(blank=True, null=True, verbose_name='Цена BYN')

    def __str__(self):
        return f' Название: {self.name} {self.price_in_currency} EUR/USD {self.price_in_byn} BYN'

    class Meta:
        verbose_name = 'Монтажные материалы'
        verbose_name_plural = 'Монтажные материалы'


class MountingMaterialsCalc(models.Model):
    order_id = models.IntegerField(verbose_name='Номер замера', blank=True, null=True)
    mounting_materials = models.ForeignKey(MountingMaterials, models.SET_NULL, verbose_name='Монтажные материалы',
                                           blank=True,
                                           null=True)
    count = models.IntegerField(default=0, verbose_name='Количество')
    price_in_byn = models.FloatField(max_length=255, default=0.0, verbose_name='Цена BYN')
    price_in_currency = models.FloatField(max_length=255, default=0.0, verbose_name='Цена EUR/USD')

    def __str__(self):
        return f' Номер замера {self.order_id} монтажный материал {self.mounting_materials}  на сумму {self.price_in_byn} BYN'

    class Meta:
        verbose_name = 'Просчет монтажных материалов'
        verbose_name_plural = 'Просчеты внутренних монтажных материалов'


class Works(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True, verbose_name='Название')
    price_in_currency = models.FloatField(blank=True, null=True, verbose_name='Цена EUR/USD')
    price_in_byn = models.FloatField(blank=True, null=True, verbose_name='Цена BYN')

    def __str__(self):
        return f' Название: {self.name} {self.price_in_currency} EUR/USD {self.price_in_byn} BYN'

    class Meta:
        verbose_name = 'Работа'
        verbose_name_plural = 'Работы'


class WorksCalc(models.Model):
    order_id = models.IntegerField(verbose_name='Номер замера', blank=True, null=True)
    works = models.ForeignKey(Works, models.SET_NULL, verbose_name='Работа',
                              blank=True,
                              null=True)
    count = models.IntegerField(default=0, verbose_name='Количество')
    price_in_byn = models.FloatField(max_length=255, default=0.0, verbose_name='Цена BYN')
    price_in_currency = models.FloatField(max_length=255, default=0.0, verbose_name='Цена EUR/USD')

    def __str__(self):
        return f' Номер замера {self.order_id} работа {self.works}  на сумму {self.price_in_byn} BYN'

    class Meta:
        verbose_name = 'Просчет работы'
        verbose_name_plural = 'Просчеты работ'


class Order(models.Model):
    STATUS = [
        {0, 'Активная заявка'},
        {1, 'Договор заключен'},
        {2, 'Думает'},
        {3, 'Придет в офис'},
        {4, 'Банковская рассрочка'},
        {5, 'Отказ до замера'},
        {6, 'Отказ после замера'}
    ]
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name='Замерщик')
    address = models.CharField(max_length=255, blank=True, null=True, verbose_name='Адрес')
    name = models.CharField(max_length=255, blank=True, null=True, verbose_name='Имя заказчика')
    phone = models.CharField(max_length=255, blank=True, null=True, verbose_name='Номер телефона')
    date = models.DateField(verbose_name='Дата замера')
    sum_materials_byn = models.FloatField(default=0.0, verbose_name='Сумма материалов в BYN')
    sum_materials_currency = models.FloatField(default=0.0, verbose_name='Сумма материалов в валюте')
    sum_works_byn = models.FloatField(default=0.0, verbose_name='Сумма работ в BYN')
    sum_works_currency = models.FloatField(default=0.0, verbose_name='Сумма работ в валюте')
    sum_byn = models.FloatField(default=0.0, verbose_name='Сумма просчета BYN')
    sum_currency = models.FloatField(default=0.0, verbose_name='Сумма просчета в EUR/USD')
    status = models.ForeignKey(Status, on_delete=models.SET_NULL, verbose_name='статус', null=True, blank=True)
    windowsill_calc = models.ManyToManyField(WindowsillCalc, blank=True, verbose_name='Просчеты подоконников')

    class Meta:
        verbose_name = 'Замер'
        verbose_name_plural = 'Замеры'

    def __str__(self):
        return f' Адрес: {self.address} Cтатус: {self.status} Сумма {self.sum_in_byn} BYN Сумма {self.sum_in_currency} EUR/USD'
