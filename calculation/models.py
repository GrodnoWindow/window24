from django.db import models
from constructor.models import Profile, Fittings, ProductType, Aggregate, SealOutside, SealRebate, SealInternal, \
    SealColor, Shpros, Shtapik, Sash, LaminationOutside, LaminationInside, ProfileWeight, Note, SupplyValve, \
    ProductsInstall, PvcSlopes, FreePositions, FavoritePositions, Windowsill, WindowsillColor, WindowsillType, LowTides, \
    LowTidesType, Visors, Flashing, FlashingMetal, Platband, ExtensionsToProfile60, ExtensionsToProfile70, \
    BayWindowToProfile60, BayWindowToProfile70, Connector90g, Accessories, Handles, Locks, StraightConnectors


class Markups(models.Model):
    windowsill = models.FloatField(default=0.0, max_length=255, verbose_name='Подоконники в %')
    low_tides = models.FloatField(default=0.0, max_length=255, verbose_name='Отливы в %')
    window = models.FloatField(default=0.0, max_length=255, verbose_name='Окна в %')

    def __str__(self):
        return f' Наценки № {self.id}'

    class Meta:
        verbose_name = 'Наценки'
        verbose_name_plural = 'Наценки'


class ExchangeRates(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя')
    value = models.FloatField(max_length=255, default=0.0, verbose_name='Значение')

    def __str__(self):
        return f'1 {self.name} = {self.value} BYN '

    class Meta:
        verbose_name = 'Курс валют'
        verbose_name_plural = 'Курсы валют'


# _______________________________ CALCULATION MODELS _______________________________
class LowTidesCalc(models.Model):
    low_tides_id = models.IntegerField(default=0.0, verbose_name="№ Отлив", blank=True, null=True)

    width = models.FloatField(max_length=255, default=0.0, verbose_name='ширина')
    length = models.FloatField(max_length=255, default=0.0, verbose_name='длинна')
    count = models.FloatField(max_length=255, default=0.0, verbose_name='количество')
    price_output = models.FloatField(max_length=255, default=0.0, verbose_name='цена')

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


class WindowsCalc(models.Model):
    discount = models.FloatField(max_length=255, verbose_name="Скидка на окно", blank=True, null=True)
    profile_id = models.IntegerField(verbose_name="Профиль id", blank=True, null=True)
    fittings_id = models.IntegerField(verbose_name="Фурнитура id ", blank=True, null=True)
    currency_name = models.CharField(max_length=255, verbose_name='Валюта имя', blank=True, null=True)
    currency_value = models.FloatField(max_length=255, verbose_name='Валюта значение НБРБ', blank=True, null=True)
    price_input = models.FloatField(max_length=255, default=0.0, verbose_name='Входная цена')
    price_output = models.FloatField(max_length=255, default=0.0, verbose_name='Выходная цена ( с наценкой )')

    def __str__(self):
        return f' Просчет окна № {self.id} на сумму {self.price_output} BYN'

    class Meta:
        verbose_name = 'Просчет окна'
        verbose_name_plural = 'Просчеты окон'


class WorkCalc(models.Model):
    work_name = models.CharField(max_length=255, verbose_name='Наименование работы', blank=True, null=True)
    work_price = models.FloatField(max_length=255, default=0.0, verbose_name='Цена работы')

    def __str__(self):
        return f' Просчет работы № {self.id} {self.work_name} на сумму {self.work_price} BYN'

    class Meta:
        verbose_name = 'Просчет работы'
        verbose_name_plural = 'Просчеты работ'


class Constructor(models.Model):
    is_active = models.BooleanField(verbose_name="Активно", default=True)
    product_type = models.ForeignKey(ProductType, on_delete=models.SET_NULL, verbose_name="Тип изделия",
                                     null=True, blank=True)
    aggregate = models.ForeignKey(Aggregate, on_delete=models.SET_NULL, verbose_name="Заполнитель №1",
                                  null=True, blank=True)
    seal_outside = models.ForeignKey(SealOutside, on_delete=models.SET_NULL,
                                     verbose_name="Уплотнение снаружи", null=True, blank=True)
    seal_rebate = models.ForeignKey(SealRebate, on_delete=models.SET_NULL,
                                    verbose_name="Уплотнение притвора", null=True, blank=True)
    seal_internal = models.ForeignKey(SealInternal, on_delete=models.SET_NULL,
                                      verbose_name="Уплотнение внутренее", null=True, blank=True)
    seal_color = models.ForeignKey(SealColor, on_delete=models.SET_NULL, verbose_name="Цвет уплотнения", null=True,
                                   blank=True)
    shpros = models.ForeignKey(Shpros, on_delete=models.SET_NULL, verbose_name="Шпрос", null=True,
                               blank=True)
    shtapik = models.ForeignKey(Shtapik, on_delete=models.SET_NULL, verbose_name="Шталик", null=True,
                                blank=True)
    sash = models.ForeignKey(Sash, on_delete=models.SET_NULL, verbose_name="Створка", null=True,
                             blank=True)
    lamination_outside = models.ForeignKey(LaminationOutside, on_delete=models.SET_NULL,
                                           verbose_name="Ламинация снаружи", null=True, blank=True)
    lamination_inside = models.ForeignKey(LaminationInside, on_delete=models.SET_NULL,
                                          verbose_name="Ланиманция внутри", null=True, blank=True)
    profile_weight = models.ForeignKey(ProfileWeight, on_delete=models.SET_NULL,
                                       verbose_name="Масса профиля", null=True, blank=True)
    note = models.ForeignKey(Note, on_delete=models.SET_NULL, verbose_name="Примечание", null=True,
                             blank=True)
    products_install = models.ForeignKey(ProductsInstall, on_delete=models.SET_NULL,
                                         verbose_name="Монтаж изделий", null=True, blank=True)
    pvc_slopes = models.ForeignKey(PvcSlopes, on_delete=models.SET_NULL, verbose_name="Откосы ПВХ",
                                   null=True, blank=True)
    free_positions = models.ForeignKey(FreePositions, on_delete=models.SET_NULL,
                                       verbose_name="Бесплатные позиции", null=True, blank=True)
    favorite_positions = models.ForeignKey(FavoritePositions, on_delete=models.SET_NULL,
                                           verbose_name="Избранные позиции", null=True, blank=True)
    windowsill = models.ForeignKey(Windowsill, on_delete=models.SET_NULL, verbose_name="Подоконники",
                                   null=True, blank=True)
    visors = models.ForeignKey(Visors, on_delete=models.SET_NULL, verbose_name="Козырьки", null=True,
                               blank=True)
    flashing = models.ForeignKey(Flashing, on_delete=models.SET_NULL, verbose_name="Нащельник",
                                 null=True, blank=True)
    flashing_metal = models.ForeignKey(FlashingMetal, on_delete=models.SET_NULL,
                                       verbose_name="Нащельник Металл", null=True, blank=True)
    platband = models.ForeignKey(Platband, on_delete=models.SET_NULL, verbose_name="Наличник",
                                 null=True, blank=True)
    extensions_to_profile60 = models.ForeignKey(ExtensionsToProfile60, on_delete=models.SET_NULL,
                                                verbose_name="Доборы к профилю 60мм", null=True, blank=True)
    extensions_to_profile70 = models.ForeignKey(ExtensionsToProfile70,
                                                on_delete=models.SET_NULL,
                                                verbose_name="Доборы к профилю 70мм", null=True, blank=True)
    bay_window_to_profile60 = models.ForeignKey(BayWindowToProfile60, on_delete=models.SET_NULL,
                                                verbose_name="Эркер к профилю 60мм", null=True, blank=True)
    bay_window_to_profile70 = models.ForeignKey(BayWindowToProfile70,
                                                on_delete=models.SET_NULL,
                                                verbose_name="Эркер к профилю 70мм", null=True, blank=True)
    connector_90g = models.ForeignKey(Connector90g, on_delete=models.SET_NULL,
                                      verbose_name="Соединитель 90гр", null=True, blank=True)
    accessories = models.ForeignKey(Accessories, on_delete=models.SET_NULL,
                                    verbose_name="Комлпектующие", null=True, blank=True)
    handles = models.ForeignKey(Handles, on_delete=models.SET_NULL,
                                verbose_name="Ручка", null=True, blank=True)
    locks = models.ForeignKey(Locks, on_delete=models.SET_NULL,
                              verbose_name="Замок", null=True, blank=True)
    straight_connectors = models.ForeignKey(StraightConnectors, on_delete=models.SET_NULL,
                                            verbose_name="Прямые соединители", null=True, blank=True)
    supply_valve = models.ForeignKey(SupplyValve, on_delete=models.SET_NULL,
                                     verbose_name="Приточный клапан", null=True, blank=True)
    price_input = models.FloatField(max_length=255, default=0.0, blank=True, null=True, verbose_name='Входная цена')
    price_window = models.FloatField(default=0.0, verbose_name='Цена окно ( с наценкой )', max_length=255, null=True,
                                     blank=True)
    price_works = models.ManyToManyField(WorkCalc, verbose_name='Работы', null=True, blank=True)
    price_material = models.FloatField(default=0.0, verbose_name='Цена материалов ( с наценкой )', max_length=255,
                                       null=True,
                                       blank=True)
    price_constructor = models.FloatField(default=0.0, verbose_name='Цена всего просчета', max_length=255, null=True,
                                          blank=True)
    window_calc = models.ForeignKey(WindowsCalc, on_delete=models.SET_NULL, verbose_name="Просчет окна", null=True,
                                    blank=True)
    windowsills_calc = models.ManyToManyField(WindowsillCalc, verbose_name="Просчеты подоконников", blank=True)
    lowtides_calc = models.ManyToManyField(LowTidesCalc, verbose_name="Просчеты отливов", blank=True)

    def __str__(self):
        return f'Просчет конструктора №{self.id}'

    class Meta:
        verbose_name = 'Просчет конструктора'
        verbose_name_plural = 'Просчеты конструкторов'
