from django.db import models
from constructor.models import Profile, Fittings, ProductType, Aggregate, SealOutside, SealRebate, SealInternal, \
    SealantColor, Shpros, Shtapik, Sash, LaminationOutside, LaminationInside, ProfileWeight, Note, SupplyValve, \
    ProductsInstall, PvcSlopes, FreePositions, Windowsill, LowTides, \
    Visors, Flashing, FlashingMetal, Platband, ExtensionsToProfile60, ExtensionsToProfile70, \
    BayWindowToProfile60, BayWindowToProfile70, Connector90g, Accessories, OtherComplectation, Locks, \
    StraightConnectors, \
    Works, TypeLamination, Sealant, Lamination, Gorbylki, Handles, ConnectionProfile, AdditionalProfile, Sealant, Door, \
    Casing, Flashing, Visors


class Markups(models.Model):
    low_tides = models.FloatField(default=0.0, max_length=255, verbose_name='Отливы ')
    low_tides_in_percent = models.BooleanField(default=True, verbose_name='считать в процентах отливы')

    window = models.FloatField(default=0.0, max_length=255, verbose_name='Окна')
    window_in_percent = models.BooleanField(default=True, verbose_name='считать в процентах окно')

    def __str__(self):
        return f' Наценки № {self.id}'

    class Meta:
        verbose_name = 'Наценки'
        verbose_name_plural = 'Наценки'


class ExchangeRates(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя')
    value = models.FloatField(max_length=255, default=0.0, verbose_name='Значение')
    auto = models.BooleanField(default=True, verbose_name='Получать автоматически')
    add_percent = models.BooleanField(default=False, verbose_name='Добавлять в процентах')
    value_percent = models.FloatField(max_length=255, default=0.0, verbose_name='Значение в процентах')

    def __str__(self):
        return f'1 {self.name} = {self.value} BYN '

    class Meta:
        verbose_name = 'Курс валют'
        verbose_name_plural = 'Курсы валют'


class Windowsill_Markups(models.Model):
    windowsill = models.ForeignKey(Windowsill, verbose_name="Подоконник", blank=True, null=True,
                                   on_delete=models.CASCADE)

    markups_diler = models.FloatField(default=0.0, max_length=255, verbose_name='Наценка диллерская')
    markups_diler_in_percent = models.BooleanField(default=True, verbose_name='Добавлять в процентах ( диллер )')

    markups_retail = models.FloatField(default=0.0, max_length=255, verbose_name='Наценка розничная')
    markups_retail_in_percent = models.BooleanField(default=True, verbose_name='Добавлять в процентах ( розница )')

    def __str__(self):
        return f' Подоконник # {self.windowsill.id} название {self.windowsill.name}, цена закупки: {self.windowsill.price_input} ,' \
               f' наценка ( дилер ): {self.markups_diler} , в процентах : {self.markups_diler_in_percent} , ' \
               f' наценка ( розница ): {self.markups_diler} , в процентах : {self.markups_retail_in_percent}'
        # return f'# {self.id} цвет: {self.color}, тип: {self.type}, цена закупки: {self.price_input}'

    class Meta:
        verbose_name = 'Наценка на подоконник'
        verbose_name_plural = 'Наценка на подоконники'


class LowTides_Markups(models.Model):
    lowtides = models.ForeignKey(LowTides, verbose_name="Отливы", blank=True, null=True,
                                 on_delete=models.CASCADE)

    markups_diler = models.FloatField(default=0.0, max_length=255, verbose_name='Наценка диллерская')
    markups_diler_in_percent = models.BooleanField(default=True, verbose_name='Добавлять в процентах ( диллер )')

    markups_retail = models.FloatField(default=0.0, max_length=255, verbose_name='Наценка розничная')
    markups_retail_in_percent = models.BooleanField(default=True, verbose_name='Добавлять в процентах ( розница )')

    def __str__(self):
        return f' Отлив № {self.lowtides.pk} название: {self.lowtides.name}, цена закупки: {self.lowtides.price_input} ,' \
               f' наценка ( дилер ): {self.markups_diler} , в процентах : {self.markups_diler_in_percent} , ' \
               f' наценка ( розница ): {self.markups_diler} , в процентах : {self.markups_retail_in_percent}'
        # return f'# {self.id} цвет: {self.color}, тип: {self.type}, цена закупки: {self.price_input}'

    class Meta:
        verbose_name = 'Наценка на отлив'
        verbose_name_plural = 'Наценка на отливы'


class Flashing_Markups(models.Model):
    flashing = models.ForeignKey(Flashing, verbose_name="Нащельник", blank=True, null=True,
                                 on_delete=models.CASCADE)

    markups_diler = models.FloatField(default=0.0, max_length=255, verbose_name='Наценка диллерская')
    markups_diler_in_percent = models.BooleanField(default=True, verbose_name='Добавлять в процентах ( диллер )')

    markups_retail = models.FloatField(default=0.0, max_length=255, verbose_name='Наценка розничная')
    markups_retail_in_percent = models.BooleanField(default=True, verbose_name='Добавлять в процентах ( розница )')

    def __str__(self):
        return f' Нащельник № {self.flashing.pk} название: {self.flashing} , цена закупки: {self.flashing.price_input} ,' \
               f' наценка ( дилер ): {self.markups_diler} , в процентах : {self.markups_diler_in_percent} , ' \
               f' наценка ( розница ): {self.markups_diler} , в процентах : {self.markups_retail_in_percent}'
        # return f'# {self.id} цвет: {self.color}, тип: {self.type}, цена закупки: {self.price_input}'

    class Meta:
        verbose_name = 'Наценка на нащельник'
        verbose_name_plural = 'Наценка на нащельники'


class Casing_Markups(models.Model):
    casing = models.ForeignKey(Casing, verbose_name="Наличник", blank=True, null=True,
                               on_delete=models.CASCADE)

    markups_diler = models.FloatField(default=0.0, max_length=255, verbose_name='Наценка диллерская')
    markups_diler_in_percent = models.BooleanField(default=True, verbose_name='Добавлять в процентах ( диллер )')

    markups_retail = models.FloatField(default=0.0, max_length=255, verbose_name='Наценка розничная')
    markups_retail_in_percent = models.BooleanField(default=True, verbose_name='Добавлять в процентах ( розница )')

    def __str__(self):
        return f' Наличник № {self.casing.pk} название: {self.casing}, цена закупки: {self.casing.price_input} ,' \
               f' наценка ( дилер ): {self.markups_diler} , в процентах : {self.markups_diler_in_percent} , ' \
               f' наценка ( розница ): {self.markups_diler} , в процентах : {self.markups_retail_in_percent}'
        # return f'# {self.id} цвет: {self.color}, тип: {self.type}, цена закупки: {self.price_input}'

    class Meta:
        verbose_name = 'Наценка на наличник'
        verbose_name_plural = 'Наценка на наличники'


class Visors_Markups(models.Model):
    visors = models.ForeignKey(Visors, verbose_name="Козырек", blank=True, null=True,
                               on_delete=models.CASCADE)

    markups_diler = models.FloatField(default=0.0, max_length=255, verbose_name='Наценка диллерская')
    markups_diler_in_percent = models.BooleanField(default=True, verbose_name='Добавлять в процентах ( диллер )')

    markups_retail = models.FloatField(default=0.0, max_length=255, verbose_name='Наценка розничная')
    markups_retail_in_percent = models.BooleanField(default=True, verbose_name='Добавлять в процентах ( розница )')

    def __str__(self):
        return f' Козырек № {self.visors.pk} название: {self.visors}, цена закупки: {self.visors.price_input} ,' \
               f' наценка ( дилер ): {self.markups_diler} , в процентах : {self.markups_diler_in_percent} , ' \
               f' наценка ( розница ): {self.markups_diler} , в процентах : {self.markups_retail_in_percent}'
        # return f'# {self.id} цвет: {self.color}, тип: {self.type}, цена закупки: {self.price_input}'

    class Meta:
        verbose_name = 'Наценка на козырек'
        verbose_name_plural = 'Наценка на козырьки'


# _______________________________ CALCULATION MODELS _______________________________
class FlashingCalc(models.Model):
    flashing_id = models.IntegerField(default=0.0, verbose_name="№ Нащельника", blank=True, null=True)

    markups_type = models.CharField(max_length=255, verbose_name='Наценка ')
    width = models.FloatField(max_length=255, default=0.0, verbose_name='Ширина')
    length = models.FloatField(max_length=255, default=0.0, verbose_name='Длинна')
    count = models.FloatField(max_length=255, default=0.0, verbose_name='Количество')
    linear_meter = models.FloatField(max_length=255, default=0.0, verbose_name='В метрах погонных')
    square_meter = models.FloatField(max_length=255, default=0.0, verbose_name='В метрах квадратных')

    price_output = models.FloatField(max_length=255, default=0.0, verbose_name='Цена')

    def __str__(self):
        return f' Нащельник № {self.pk} длинна {self.length} / ширина {self.width} = {self.price_output} BYN'

    class Meta:
        verbose_name = 'Просчет нащельника'
        verbose_name_plural = 'Просчеты нащельников'


class CasingCalc(models.Model):
    casing_id = models.IntegerField(default=0.0, verbose_name="№ Наличник", blank=True, null=True)

    markups_type = models.CharField(max_length=255, verbose_name='Наценка ')
    width = models.FloatField(max_length=255, default=0.0, verbose_name='Ширина')
    length = models.FloatField(max_length=255, default=0.0, verbose_name='Длинна')
    count = models.FloatField(max_length=255, default=0.0, verbose_name='Количество')
    linear_meter = models.FloatField(max_length=255, default=0.0, verbose_name='В метрах погонных')
    square_meter = models.FloatField(max_length=255, default=0.0, verbose_name='В метрах квадратных')

    price_output = models.FloatField(max_length=255, default=0.0, verbose_name='Цена')

    def __str__(self):
        return f' Наличник № {self.pk} длинна {self.length} / ширина {self.width} = {self.price_output} BYN'

    class Meta:
        verbose_name = 'Просчет наличника'
        verbose_name_plural = 'Просчеты наличников'


class VisorsCalc(models.Model):
    visors_id = models.IntegerField(default=0.0, verbose_name="№ Козырька", blank=True, null=True)

    markups_type = models.CharField(max_length=255, verbose_name='Наценка ')
    width = models.FloatField(max_length=255, default=0.0, verbose_name='Ширина')
    length = models.FloatField(max_length=255, default=0.0, verbose_name='Длинна')
    count = models.FloatField(max_length=255, default=0.0, verbose_name='Количество')
    linear_meter = models.FloatField(max_length=255, default=0.0, verbose_name='В метрах погонных')
    square_meter = models.FloatField(max_length=255, default=0.0, verbose_name='В метрах квадратных')

    price_output = models.FloatField(max_length=255, default=0.0, verbose_name='Цена')

    def __str__(self):
        return f' Наличник № {self.pk} длинна {self.length} / ширина {self.width} = {self.price_output} BYN'

    class Meta:
        verbose_name = 'Просчет наличника'
        verbose_name_plural = 'Просчеты наличников'


class LowTidesCalc(models.Model):
    low_tides_id = models.IntegerField(default=0.0, verbose_name="№ Отлив", blank=True, null=True)

    markups_type = models.CharField(max_length=255, verbose_name='Наценка ')
    width = models.FloatField(max_length=255, default=0.0, verbose_name='Ширина')
    length = models.FloatField(max_length=255, default=0.0, verbose_name='Длинна')
    count = models.FloatField(max_length=255, default=0.0, verbose_name='количество')
    linear_meter = models.FloatField(max_length=255, default=0.0, verbose_name='В метрах погонных')
    square_meter = models.FloatField(max_length=255, default=0.0, verbose_name='В метрах квадратных')

    price_output = models.FloatField(max_length=255, default=0.0, verbose_name='цена')

    def __str__(self):
        return f' Отлив № {self.id} длинна {self.length} / ширина {self.width} = {self.price_output} BYN'

    class Meta:
        verbose_name = 'Просчет отлива'
        verbose_name_plural = 'Просчеты отливов'


class WindowsillCalc(models.Model):
    windowsill_id = models.IntegerField(default=0.0, verbose_name="№ Подоконник", blank=True, null=True)

    plug = models.IntegerField(default=0, verbose_name='Заглушка', blank=True, null=True)
    connector = models.IntegerField(default=0, verbose_name='Соединитель', blank=True, null=True)

    markups_type = models.CharField(max_length=255, verbose_name='Наценка')
    width = models.FloatField(max_length=255, default=0.0, verbose_name='Ширина')
    length = models.FloatField(max_length=255, default=0.0, verbose_name='Длинна')
    count = models.FloatField(max_length=255, default=0.0, verbose_name='Количество')
    square_meter = models.FloatField(max_length=255, default=0.0, verbose_name='В метрах квадратных')
    linear_meter = models.FloatField(max_length=255, default=0.0, verbose_name='В метрах погонных')

    price_output = models.FloatField(max_length=255, default=0.0, verbose_name='Цена')

    def __str__(self):
        return f' Подоконник № {self.id}  на сумму {self.price_output} BYN'

    class Meta:
        verbose_name = 'Просчет подоконника'
        verbose_name_plural = 'Просчеты подоконников'


class WindowDiscountMarkups(models.Model):
    profile_id = models.ForeignKey(Profile, verbose_name="Профиль", blank=True, null=True, on_delete=models.CASCADE)
    fittings_id = models.ForeignKey(Fittings, verbose_name="Фурнитура", blank=True, null=True, on_delete=models.CASCADE)
    discount = models.FloatField(max_length=255, default=0.0, verbose_name='Значение')

    markups = models.FloatField(default=0.0, max_length=255, verbose_name='Наценка')
    markups_in_percent = models.BooleanField(default=True, verbose_name='Добавлять в процентах')

    def __str__(self):
        return f'Профиль : {self.profile_id.name} + Фурнитура: скидка {self.fittings_id.name} = {self.discount} %,' \
               f' Наценка : {self.markups}, В процентах: {self.markups_in_percent}'

    class Meta:
        verbose_name = 'Скидка/Наценка на окно'
        verbose_name_plural = 'Скидки/Наценки на окна'


class WindowsCalc(models.Model):
    discount = models.FloatField(max_length=255, verbose_name="Скидка на окно", blank=True, null=True)
    profile_id = models.IntegerField(verbose_name="Профиль id", blank=True, null=True)
    fittings_id = models.IntegerField(verbose_name="Фурнитура id ", blank=True, null=True)
    currency_name = models.CharField(max_length=255, verbose_name='Валюта имя', blank=True, null=True)
    currency_value = models.FloatField(max_length=255, verbose_name='Валюта значение НБРБ', blank=True, null=True)
    price_input = models.FloatField(max_length=255, default=0.0, verbose_name='Входная цена')
    price_output = models.FloatField(max_length=255, default=0.0, verbose_name='Выходная цена ( с наценкой )')

    markup_value = models.FloatField(max_length=255, default=0.0, verbose_name='Значение наценки')
    markup_percent = models.BooleanField(default=True, verbose_name='Наценка в процентах')

    def __str__(self):
        return f' Просчет окна № {self.pk} на сумму {self.price_output} BYN'

    class Meta:
        verbose_name = 'Просчет окна'
        verbose_name_plural = 'Просчеты окон'


class Constructor(models.Model):
    # EQUIPMENT
    product_type = models.ForeignKey(ProductType, on_delete=models.SET_NULL, verbose_name="Тип изделия",
                                     null=True, blank=True)
    door = models.ForeignKey(Door, on_delete=models.SET_NULL, verbose_name='Двери', null=True, blank=True)
    aggregate = models.ForeignKey(Aggregate, on_delete=models.SET_NULL, verbose_name="Заполнитель",
                                  null=True, blank=True)
    # EQUIPMENT END
    # MATERIALS
    lamination = models.ForeignKey(Lamination, on_delete=models.SET_NULL, verbose_name="Ламинация", null=True,
                                   blank=True)

    shtapik = models.ForeignKey(Shtapik, on_delete=models.SET_NULL, verbose_name="Штапик", null=True, blank=True)
    sash = models.ForeignKey(Sash, on_delete=models.SET_NULL, verbose_name="Створка", null=True, blank=True)
    gorbylki = models.ForeignKey(Gorbylki, on_delete=models.SET_NULL, verbose_name="Горбыльки", null=True, blank=True)
    handles = models.ForeignKey(Handles, on_delete=models.SET_NULL, verbose_name="Ручки", null=True, blank=True)
    connection_profile = models.ForeignKey(ConnectionProfile, on_delete=models.SET_NULL,
                                           verbose_name="Соединительные профиля", null=True, blank=True)
    additional_profile = models.ForeignKey(AdditionalProfile, on_delete=models.SET_NULL,
                                           verbose_name="Доборные профиля", null=True, blank=True)
    sealant = models.ForeignKey(Sealant, on_delete=models.SET_NULL, verbose_name="Уплотнитель", null=True, blank=True)
    other_complectation = models.ForeignKey(OtherComplectation, on_delete=models.SET_NULL,
                                            verbose_name="Прочее комплектующие", null=True, blank=True)

    price_constructor = models.FloatField(default=0.0, verbose_name='Цена всего просчета', max_length=255, null=True,
                                          blank=True)
    # MATERIALS END
    window_calc = models.ForeignKey(WindowsCalc, on_delete=models.SET_NULL, verbose_name="Просчет окна", null=True,
                                    blank=True)
    windowsills_calc = models.ManyToManyField(WindowsillCalc, verbose_name="Просчеты подоконников", blank=True)
    lowtides_calc = models.ManyToManyField(LowTidesCalc, verbose_name="Просчеты отливов", blank=True)
    flashing_calc = models.ManyToManyField(FlashingCalc, verbose_name="Просчеты нащельников", blank=True)
    visors_calc = models.ManyToManyField(VisorsCalc, verbose_name="Просчеты козырьков", blank=True)
    casing_calc = models.ManyToManyField(CasingCalc, verbose_name="Просчеты наличников", blank=True)
    works = models.ManyToManyField(Works, verbose_name='Работы', blank=True)

    def __str__(self):
        return f'Просчет конструктора №{self.pk} на сумму {self.price_constructor}'

    class Meta:
        verbose_name = 'Просчет конструктора'
        verbose_name_plural = 'Просчеты конструкторов'
