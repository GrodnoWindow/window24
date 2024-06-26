from django.db import models
from constructor.models import Profile, Fittings, ProductType, Aggregate, \
    Shtapik, Sash, Windowsill, LowTides, OtherComplectation, SlopesOfMetal, InternalSlope, \
    Works, Lamination, Gorbylki, Handles, ConnectionProfile, AdditionalProfile, Sealant, Door, \
    Casing, Flashing, Visors, LowTidesType, OtherComplectationProfile
from users.models import User


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


class WindowsillMarkups(models.Model):
    windowsill = models.ForeignKey(Windowsill, verbose_name="Подоконник", blank=True, null=True,
                                   on_delete=models.CASCADE)

    markups_diler = models.FloatField(default=0.0, max_length=255, verbose_name='Наценка диллерская')
    markups_diler_in_percent = models.BooleanField(default=True, verbose_name='Добавлять в процентах ( диллер )')

    markups_retail = models.FloatField(default=0.0, max_length=255, verbose_name='Наценка розничная')
    markups_retail_in_percent = models.BooleanField(default=True, verbose_name='Добавлять в процентах ( розница )')

    markups_3 = models.FloatField(default=0.0, max_length=255, verbose_name='Наценка №3')
    markups_3_in_percent = models.BooleanField(default=True, verbose_name='Добавлять в процентах ( наценка №3 )')

    markups_4 = models.FloatField(default=0.0, max_length=255, verbose_name='Наценка №4')
    markups_4_in_percent = models.BooleanField(default=True, verbose_name='Добавлять в процентах ( наценка №4 )')

    markups_5 = models.FloatField(default=0.0, max_length=255, verbose_name='Наценка №5')
    markups_5_in_percent = models.BooleanField(default=True, verbose_name='Добавлять в процентах ( наценка №5 )')

    def __str__(self):
        return f' Подоконник # {self.windowsill.id} название {self.windowsill.name}, цена закупки: {self.windowsill.price_input} ,'

    class Meta:
        verbose_name = 'Наценка на подоконник'
        verbose_name_plural = 'Наценка на подоконники'

class AdditionalProfileMarkups(models.Model):
    additional_profile = models.ForeignKey(AdditionalProfile, verbose_name="Доборный профиль", blank=True, null=True,
                                   on_delete=models.CASCADE)

    markups_diler = models.FloatField(default=0.0, max_length=255, verbose_name='Наценка диллерская')
    markups_diler_in_percent = models.BooleanField(default=True, verbose_name='Добавлять в процентах ( диллер )')

    markups_retail = models.FloatField(default=0.0, max_length=255, verbose_name='Наценка розничная')
    markups_retail_in_percent = models.BooleanField(default=True, verbose_name='Добавлять в процентах ( розница )')

    markups_3 = models.FloatField(default=0.0, max_length=255, verbose_name='Наценка №3')
    markups_3_in_percent = models.BooleanField(default=True, verbose_name='Добавлять в процентах ( наценка №3 )')

    markups_4 = models.FloatField(default=0.0, max_length=255, verbose_name='Наценка №4')
    markups_4_in_percent = models.BooleanField(default=True, verbose_name='Добавлять в процентах ( наценка №4 )')

    markups_5 = models.FloatField(default=0.0, max_length=255, verbose_name='Наценка №5')
    markups_5_in_percent = models.BooleanField(default=True, verbose_name='Добавлять в процентах ( наценка №5 )')

    def __str__(self):
        return f' Подоконник # {self.additional_profile.id} название {self.additional_profile}, цена закупки: {self.additional_profile.price_input} ,'

    class Meta:
        verbose_name = 'Наценка на доборные профиля'
        verbose_name_plural = 'Наценка на доборные профиля'

class ConnectionProfileMarkups(models.Model):
    connection_profile = models.ForeignKey(ConnectionProfile, verbose_name="Соединительные профиль", blank=True, null=True,
                                   on_delete=models.CASCADE)

    markups_diler = models.FloatField(default=0.0, max_length=255, verbose_name='Наценка диллерская')
    markups_diler_in_percent = models.BooleanField(default=True, verbose_name='Добавлять в процентах ( диллер )')

    markups_retail = models.FloatField(default=0.0, max_length=255, verbose_name='Наценка розничная')
    markups_retail_in_percent = models.BooleanField(default=True, verbose_name='Добавлять в процентах ( розница )')

    markups_3 = models.FloatField(default=0.0, max_length=255, verbose_name='Наценка №3')
    markups_3_in_percent = models.BooleanField(default=True, verbose_name='Добавлять в процентах ( наценка №3 )')

    markups_4 = models.FloatField(default=0.0, max_length=255, verbose_name='Наценка №4')
    markups_4_in_percent = models.BooleanField(default=True, verbose_name='Добавлять в процентах ( наценка №4 )')

    markups_5 = models.FloatField(default=0.0, max_length=255, verbose_name='Наценка №5')
    markups_5_in_percent = models.BooleanField(default=True, verbose_name='Добавлять в процентах ( наценка №5 )')

    def __str__(self):
        return f' Подоконник # {self.connection_profile.id} название {self.connection_profile.name}, цена закупки: {self.connection_profile.price_input} ,'

    class Meta:
        verbose_name = 'Наценка на соединительные профиля'
        verbose_name_plural = 'Наценка на соединительные профиля'


class OtherComplectationProfileMarkups(models.Model):
    other_complectation_profile = models.ForeignKey(OtherComplectationProfile, verbose_name="Доп комп. профиль", blank=True, null=True,
                                   on_delete=models.CASCADE)

    markups_diler = models.FloatField(default=0.0, max_length=255, verbose_name='Наценка диллерская')
    markups_diler_in_percent = models.BooleanField(default=True, verbose_name='Добавлять в процентах ( диллер )')

    markups_retail = models.FloatField(default=0.0, max_length=255, verbose_name='Наценка розничная')
    markups_retail_in_percent = models.BooleanField(default=True, verbose_name='Добавлять в процентах ( розница )')

    markups_3 = models.FloatField(default=0.0, max_length=255, verbose_name='Наценка №3')
    markups_3_in_percent = models.BooleanField(default=True, verbose_name='Добавлять в процентах ( наценка №3 )')

    markups_4 = models.FloatField(default=0.0, max_length=255, verbose_name='Наценка №4')
    markups_4_in_percent = models.BooleanField(default=True, verbose_name='Добавлять в процентах ( наценка №4 )')

    markups_5 = models.FloatField(default=0.0, max_length=255, verbose_name='Наценка №5')
    markups_5_in_percent = models.BooleanField(default=True, verbose_name='Добавлять в процентах ( наценка №5 )')

    def __str__(self):
        return f' Подоконник # {self.other_complectation_profile.id} название {self.other_complectation_profile.name}, цена закупки: {self.other_complectation_profile.price_input} ,'

    class Meta:
        verbose_name = 'Наценка на доп комп. профиля'
        verbose_name_plural = 'Наценка на доп комп. профиля'
class LowTidesMarkups(models.Model):
    lowtides = models.ForeignKey(LowTides, verbose_name="Отливы", blank=True, null=True,
                                 on_delete=models.CASCADE)

    markups_diler = models.FloatField(default=0.0, max_length=255, verbose_name='Наценка диллерская')
    markups_diler_in_percent = models.BooleanField(default=True, verbose_name='Добавлять в процентах ( диллер )')

    markups_retail = models.FloatField(default=0.0, max_length=255, verbose_name='Наценка розничная')
    markups_retail_in_percent = models.BooleanField(default=True, verbose_name='Добавлять в процентах ( розница )')

    markups_3 = models.FloatField(default=0.0, max_length=255, verbose_name='Наценка №3')
    markups_3_in_percent = models.BooleanField(default=True, verbose_name='Добавлять в процентах ( наценка №3 )')

    markups_4 = models.FloatField(default=0.0, max_length=255, verbose_name='Наценка №4')
    markups_4_in_percent = models.BooleanField(default=True, verbose_name='Добавлять в процентах ( наценка №4 )')

    markups_5 = models.FloatField(default=0.0, max_length=255, verbose_name='Наценка №5')
    markups_5_in_percent = models.BooleanField(default=True, verbose_name='Добавлять в процентах ( наценка №5 )')

    def __str__(self):
        return f' Отлив № {self.lowtides.pk} название: {self.lowtides.name}, цена закупки: {self.lowtides.price_input} ,'

    class Meta:
        verbose_name = 'Наценка на отлив'
        verbose_name_plural = 'Наценка на отливы'


class FlashingMarkups(models.Model):
    flashing = models.ForeignKey(Flashing, verbose_name="Нащельник", blank=True, null=True,
                                 on_delete=models.CASCADE)

    markups_diler = models.FloatField(default=0.0, max_length=255, verbose_name='Наценка диллерская')
    markups_diler_in_percent = models.BooleanField(default=True, verbose_name='Добавлять в процентах ( диллер )')

    markups_retail = models.FloatField(default=0.0, max_length=255, verbose_name='Наценка розничная')
    markups_retail_in_percent = models.BooleanField(default=True, verbose_name='Добавлять в процентах ( розница )')

    markups_3 = models.FloatField(default=0.0, max_length=255, verbose_name='Наценка №3')
    markups_3_in_percent = models.BooleanField(default=True, verbose_name='Добавлять в процентах ( наценка №3 )')

    markups_4 = models.FloatField(default=0.0, max_length=255, verbose_name='Наценка №4')
    markups_4_in_percent = models.BooleanField(default=True, verbose_name='Добавлять в процентах ( наценка №4 )')

    markups_5 = models.FloatField(default=0.0, max_length=255, verbose_name='Наценка №5')
    markups_5_in_percent = models.BooleanField(default=True, verbose_name='Добавлять в процентах ( наценка №5 )')

    def __str__(self):
        return f' Нащельник № {self.flashing.pk} название: {self.flashing} , цена закупки: {self.flashing.price_input} ,'

    class Meta:
        verbose_name = 'Наценка на нащельник'
        verbose_name_plural = 'Наценка на нащельники'


class CasingMarkups(models.Model):
    casing = models.ForeignKey(Casing, verbose_name="Наличник", blank=True, null=True,
                               on_delete=models.CASCADE)

    markups_diler = models.FloatField(default=0.0, max_length=255, verbose_name='Наценка диллерская')
    markups_diler_in_percent = models.BooleanField(default=True, verbose_name='Добавлять в процентах ( диллер )')

    markups_retail = models.FloatField(default=0.0, max_length=255, verbose_name='Наценка розничная')
    markups_retail_in_percent = models.BooleanField(default=True, verbose_name='Добавлять в процентах ( розница )')

    markups_3 = models.FloatField(default=0.0, max_length=255, verbose_name='Наценка №3')
    markups_3_in_percent = models.BooleanField(default=True, verbose_name='Добавлять в процентах ( наценка №3 )')

    markups_4 = models.FloatField(default=0.0, max_length=255, verbose_name='Наценка №4')
    markups_4_in_percent = models.BooleanField(default=True, verbose_name='Добавлять в процентах ( наценка №4 )')

    markups_5 = models.FloatField(default=0.0, max_length=255, verbose_name='Наценка №5')
    markups_5_in_percent = models.BooleanField(default=True, verbose_name='Добавлять в процентах ( наценка №5 )')

    def __str__(self):
        return f' Наличник № {self.casing.pk} название: {self.casing}'

    class Meta:
        verbose_name = 'Наценка на наличник'
        verbose_name_plural = 'Наценка на наличники'


class VisorsMarkups(models.Model):
    visors = models.ForeignKey(Visors, verbose_name="Козырек", blank=True, null=True,
                               on_delete=models.CASCADE)

    markups_diler = models.FloatField(default=0.0, max_length=255, verbose_name='Наценка диллерская')
    markups_diler_in_percent = models.BooleanField(default=True, verbose_name='Добавлять в процентах ( диллер )')

    markups_retail = models.FloatField(default=0.0, max_length=255, verbose_name='Наценка розничная')
    markups_retail_in_percent = models.BooleanField(default=True, verbose_name='Добавлять в процентах ( розница )')

    markups_3 = models.FloatField(default=0.0, max_length=255, verbose_name='Наценка №3')
    markups_3_in_percent = models.BooleanField(default=True, verbose_name='Добавлять в процентах ( наценка №3 )')

    markups_4 = models.FloatField(default=0.0, max_length=255, verbose_name='Наценка №4')
    markups_4_in_percent = models.BooleanField(default=True, verbose_name='Добавлять в процентах ( наценка №4 )')

    markups_5 = models.FloatField(default=0.0, max_length=255, verbose_name='Наценка №5')
    markups_5_in_percent = models.BooleanField(default=True, verbose_name='Добавлять в процентах ( наценка №5 )')

    def __str__(self):
        return f' Козырек № {self.visors.pk} название: {self.visors}, цена закупки: {self.visors.price_input} ,'

    class Meta:
        verbose_name = 'Наценка на козырек'
        verbose_name_plural = 'Наценка на козырьки'


class SlopesOfMetalMarkups(models.Model):
    slopes_of_metal = models.ForeignKey(SlopesOfMetal, verbose_name="Откосы из металла", blank=True, null=True,
                                        on_delete=models.CASCADE)

    markups_diler = models.FloatField(default=0.0, max_length=255, verbose_name='Наценка диллерская')
    markups_diler_in_percent = models.BooleanField(default=True, verbose_name='Добавлять в процентах ( диллер )')

    markups_retail = models.FloatField(default=0.0, max_length=255, verbose_name='Наценка розничная')
    markups_retail_in_percent = models.BooleanField(default=True, verbose_name='Добавлять в процентах ( розница )')

    markups_3 = models.FloatField(default=0.0, max_length=255, verbose_name='Наценка №3')
    markups_3_in_percent = models.BooleanField(default=True, verbose_name='Добавлять в процентах ( наценка №3 )')

    markups_4 = models.FloatField(default=0.0, max_length=255, verbose_name='Наценка №4')
    markups_4_in_percent = models.BooleanField(default=True, verbose_name='Добавлять в процентах ( наценка №4 )')

    markups_5 = models.FloatField(default=0.0, max_length=255, verbose_name='Наценка №5')
    markups_5_in_percent = models.BooleanField(default=True, verbose_name='Добавлять в процентах ( наценка №5 )')

    def __str__(self):
        return f' Откос из металла № {self.slopes_of_metal.pk} название: {self.slopes_of_metal}, цена закупки: {self.slopes_of_metal.price_input} ,'

    class Meta:
        verbose_name = 'Наценка на откосы из металла'
        verbose_name_plural = 'Наценка на откосы из металла'


class InternalSlopeMarkups(models.Model):
    internal_slope = models.ForeignKey(InternalSlope, verbose_name="Внутренние откосы", blank=True, null=True,
                                       on_delete=models.CASCADE)

    markups_diler = models.FloatField(default=0.0, max_length=255, verbose_name='Наценка диллерская')
    markups_diler_in_percent = models.BooleanField(default=True, verbose_name='Добавлять в процентах ( диллер )')

    markups_retail = models.FloatField(default=0.0, max_length=255, verbose_name='Наценка розничная')
    markups_retail_in_percent = models.BooleanField(default=True, verbose_name='Добавлять в процентах ( розница )')

    markups_3 = models.FloatField(default=0.0, max_length=255, verbose_name='Наценка №3')
    markups_3_in_percent = models.BooleanField(default=True, verbose_name='Добавлять в процентах ( наценка №3 )')

    markups_4 = models.FloatField(default=0.0, max_length=255, verbose_name='Наценка №4')
    markups_4_in_percent = models.BooleanField(default=True, verbose_name='Добавлять в процентах ( наценка №4 )')

    markups_5 = models.FloatField(default=0.0, max_length=255, verbose_name='Наценка №5')
    markups_5_in_percent = models.BooleanField(default=True, verbose_name='Добавлять в процентах ( наценка №5 )')

    def __str__(self):
        return f'Внутрненние откосы № {self.internal_slope.pk} название: {self.internal_slope}, цена закупки: {self.internal_slope.price_input} ,'

    class Meta:
        verbose_name = 'Наценка на внутренние откосы'
        verbose_name_plural = 'Наценка на внутренние откосы'


class Works_Markups(models.Model):
    work = models.ForeignKey(Works, verbose_name="Работа", blank=True, null=True,
                             on_delete=models.CASCADE)

    markups = models.FloatField(default=0.0, max_length=255, verbose_name='Наценка на работу')

    def __str__(self):
        return f' Работа № {self.work.id} название {self.work.name}' \
               f' наценка : {self.markup} '

    class Meta:
        verbose_name = 'Наценка на подоконник'
        verbose_name_plural = 'Наценка на подоконники'


# _______________________________ CALCULATION MODELS _______________________________

class FlashingInstallation(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название монтажа", blank=True, null=True)
    value = models.FloatField(default=0.0, verbose_name="Стоимость монтажа", blank=True, null=True)

    def __str__(self):
        return f' Монтаж {self.name} цена {self.value} BYN'

    class Meta:
        verbose_name = 'Монтаж нащельников'
        verbose_name_plural = 'Монтажи нащельников'


class FlashingCalc(models.Model):
    flashing_id = models.IntegerField(default=0.0, verbose_name="№ Нащельника", blank=True, null=True)

    installation_id = models.IntegerField(default=0, verbose_name='Установка', blank=True, null=True)
    color_id = models.IntegerField(default=0, verbose_name='Цвет', blank=True, null=True)

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


class CasingInstallation(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название монтажа", blank=True, null=True)
    value = models.FloatField(default=0.0, verbose_name="Стоимость монтажа", blank=True, null=True)

    def __str__(self):
        return f' Монтаж {self.name} цена {self.value} BYN'

    class Meta:
        verbose_name = 'Монтаж наличников'
        verbose_name_plural = 'Монтажи наличникв'


class CasingCalc(models.Model):
    casing_id = models.IntegerField(default=0.0, verbose_name="№ Наличник", blank=True, null=True)

    installation_id = models.IntegerField(default=0, verbose_name='Установка', blank=True, null=True)
    color_id = models.IntegerField(default=0, verbose_name='Цвет', blank=True, null=True)
    fastening_id = models.CharField(max_length=255, verbose_name='Крепление', blank=True, null=True)

    markups_type = models.CharField(max_length=255, verbose_name='Наценка ')
    width = models.FloatField(max_length=255, default=0.0, verbose_name='Ширина')
    nipel_count = models.FloatField(max_length=255, default=0.0, verbose_name='Количество Нипелей')
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


class VisorsInstallation(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название монтажа", blank=True, null=True)
    value = models.FloatField(default=0.0, verbose_name="Стоимость монтажа", blank=True, null=True)

    def __str__(self):
        return f' Монтаж {self.name} цена {self.value} BYN'

    class Meta:
        verbose_name = 'Монтаж козырька'
        verbose_name_plural = 'Монтажи козырьков'


class VisorsCalc(models.Model):
    visors_id = models.IntegerField(default=0.0, verbose_name="№ Козырька", blank=True, null=True)

    installation_id = models.IntegerField(default=0, verbose_name='Установка', blank=True, null=True)
    color_id = models.IntegerField(default=0, verbose_name='Цвет', blank=True, null=True)

    markups_type = models.CharField(max_length=255, verbose_name='Наценка ')
    width = models.FloatField(max_length=255, default=0.0, verbose_name='Ширина')
    width_1 = models.FloatField(max_length=255, default=0.0, verbose_name='Ширина 1')
    width_2 = models.FloatField(max_length=255, default=0.0, verbose_name='Ширина 2')
    width_3 = models.FloatField(max_length=255, default=0.0, verbose_name='Ширина 3')
    length = models.FloatField(max_length=255, default=0.0, verbose_name='Длинна')
    count = models.FloatField(max_length=255, default=0.0, verbose_name='Количество')
    linear_meter = models.FloatField(max_length=255, default=0.0, verbose_name='В метрах погонных')
    square_meter = models.FloatField(max_length=255, default=0.0, verbose_name='В метрах квадратных')

    price_output = models.FloatField(max_length=255, default=0.0, verbose_name='Цена')

    def __str__(self):
        return f' Наличник № {self.pk} длинна {self.length} / ширина {self.width} = {self.price_output} BYN'

    class Meta:
        verbose_name = 'Просчет козырька'
        verbose_name_plural = 'Просчеты козырьков'


class AdditionalProfileCalc(models.Model):
    additional_profile_id = models.IntegerField(default=0.0, verbose_name="№ доборного профиля", blank=True, null=True)

    markups_type = models.CharField(max_length=255, verbose_name='Наценка ')
    length = models.FloatField(max_length=255, default=0.0, verbose_name='Длинна')
    count = models.FloatField(max_length=255, default=0.0, verbose_name='Количество')
    linear_meter = models.FloatField(max_length=255, default=0.0, verbose_name='В метрах погонных')
    markups_type = models.CharField(max_length=255, verbose_name='Наценка ')

    price_output = models.FloatField(max_length=255, default=0.0, verbose_name='Цена')

    def __str__(self):
        return f' Добрный профиль № {self.pk} {self.price_output} BYN'

    class Meta:
        verbose_name = 'Просчет доборного профиля'
        verbose_name_plural = 'Просчеты доборных профилей'

class ConnectionProfileCalc(models.Model):
    connection_profile_id = models.IntegerField(default=0.0, verbose_name="№ соединительного профиля", blank=True, null=True)

    markups_type = models.CharField(max_length=255, verbose_name='Наценка ')
    length = models.FloatField(max_length=255, default=0.0, verbose_name='Длинна')
    count = models.FloatField(max_length=255, default=0.0, verbose_name='Количество')
    linear_meter = models.FloatField(max_length=255, default=0.0, verbose_name='В метрах погонных')

    price_output = models.FloatField(max_length=255, default=0.0, verbose_name='Цена')

    def __str__(self):
        return f' Соединительный профиль № {self.pk} длинна {self.length} = {self.price_output} BYN'

    class Meta:
        verbose_name = 'Просчет соединительного профиля'
        verbose_name_plural = 'Просчеты соединительных профилей'


class OtherComplectationProfileCalc(models.Model):
    other_complectation_profile_id = models.IntegerField(default=0.0, verbose_name="№ Доп комп. профиля", blank=True, null=True)

    markups_type = models.CharField(max_length=255, verbose_name='Наценка ')
    length = models.FloatField(max_length=255, default=0.0, verbose_name='Длинна')
    count = models.FloatField(max_length=255, default=0.0, verbose_name='Количество')
    linear_meter = models.FloatField(max_length=255, default=0.0, verbose_name='В метрах погонных')

    price_output = models.FloatField(max_length=255, default=0.0, verbose_name='Цена')

    def __str__(self):
        return f' Доп комп. профиль № {self.pk} длинна {self.length} = {self.price_output} BYN'

    class Meta:
        verbose_name = 'Просчет доп комп. профиля'
        verbose_name_plural = 'Просчеты доп комп. профилей'
class LowTidesInstallation(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название монтажа", blank=True, null=True)
    value = models.FloatField(default=0.0, verbose_name="Стоимость монтажа", blank=True, null=True)

    def __str__(self):
        return f' Монтаж {self.name} цена {self.value} BYN'

    class Meta:
        verbose_name = 'Монтаж отлива'
        verbose_name_plural = 'Монтажи отливов'


class LowTidesCalc(models.Model):
    low_tides_id = models.IntegerField(default=0.0, verbose_name="№ Отлив", blank=True, null=True)

    installation_id = models.IntegerField(default=0, verbose_name='Установка', blank=True, null=True)
    color_id = models.IntegerField(default=0, verbose_name='Цвет', blank=True, null=True)
    low_tides_type = models.ForeignKey(LowTidesType, verbose_name='Тип отлива', blank=True, null=True, on_delete=models.SET_NULL)
    width_1 = models.IntegerField(blank=True,null=True,verbose_name='Ширина 1')
    width_2 = models.IntegerField(blank=True,null=True,verbose_name='Ширина 2')
    width_3 = models.IntegerField(blank=True,null=True,verbose_name='Ширина 3')
    plug = models.IntegerField(default=0, verbose_name='Заглушка', blank=True, null=True)
    width = models.FloatField(max_length=255, default=0.0, verbose_name='Ширина')
    length = models.FloatField(max_length=255, default=0.0, verbose_name='Длинна')
    count = models.FloatField(max_length=255, default=0.0, verbose_name='количество')
    linear_meter = models.FloatField(max_length=255, default=0.0, verbose_name='В метрах погонных')
    square_meter = models.FloatField(max_length=255, default=0.0, verbose_name='В метрах квадратных')
    markups_type = models.CharField(max_length=255, verbose_name='Наценка ')

    price_output = models.FloatField(max_length=255, default=0.0, verbose_name='цена')

    def __str__(self):
        return f' Отлив № {self.id} длинна {self.length} / ширина {self.width} = {self.price_output} BYN'

    class Meta:
        verbose_name = 'Просчет отлива'
        verbose_name_plural = 'Просчеты отливов'


class WindowsillInstallation(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название монтажа", blank=True, null=True)
    value = models.FloatField(default=0.0, verbose_name="Стоимость монтажа", blank=True, null=True)

    def __str__(self):
        return f' Монтаж {self.name} цена {self.value} BYN'

    class Meta:
        verbose_name = 'Монтаж подоконников'
        verbose_name_plural = 'Монтажи подоконников'


class WindowsillCalc(models.Model):
    windowsill_id = models.IntegerField(default=0.0, verbose_name="№ Подоконник", blank=True, null=True)

    installation_id = models.IntegerField(default=0, verbose_name='Установка', blank=True, null=True)
    color_id = models.IntegerField(default=0, verbose_name='Цвет', blank=True, null=True)

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


class SlopesOfMetalInstallation(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название монтажа", blank=True, null=True)
    value = models.FloatField(default=0.0, verbose_name="Стоимость монтажа", blank=True, null=True)

    def __str__(self):
        return f' Монтаж {self.name} цена {self.value} BYN'

    class Meta:
        verbose_name = 'Монтаж откосов из металла'
        verbose_name_plural = 'Монтажи откосов из металла'


class SlopesOfMetalCalc(models.Model):
    slopes_of_metal_id = models.IntegerField(default=0.0, verbose_name="№ Откоса из металла", blank=True, null=True)

    installation_id = models.IntegerField(default=0, verbose_name='Установка', blank=True, null=True)
    color_id = models.IntegerField(default=0, verbose_name='Цвет', blank=True, null=True)

    markups_type = models.CharField(max_length=255, verbose_name='Наценка')
    width = models.IntegerField(default=0,blank=True,null=True, verbose_name='Ширина')
    width_1 = models.IntegerField(default=0,blank=True,null=True, verbose_name='Ширина 1')
    width_2 = models.IntegerField(default=0,blank=True,null=True, verbose_name='Ширина 2')
    width_3 = models.IntegerField(default=0,blank=True,null=True, verbose_name='Ширина 3')
    width_4 = models.IntegerField(default=0,blank=True,null=True, verbose_name='Ширина 4')

    lock_width = models.IntegerField(default=0,blank=True,null=True, verbose_name='Замок ширина ( общая )')
    lock_length = models.IntegerField(default=0,blank=True,null=True, verbose_name='Замок длинна ( общая )')
    lock_width_1 = models.IntegerField(default=0,blank=True,null=True, verbose_name='Замок ширина 1')
    lock_width_2 = models.IntegerField(default=0,blank=True,null=True, verbose_name='Замок ширина 2')
    lock_width_3 = models.IntegerField(default=0,blank=True,null=True, verbose_name='Замок ширина 3')
    lock_width_4 = models.IntegerField(default=0,blank=True,null=True, verbose_name='Замок ширина 4')

    low_tides_width = models.IntegerField(default=0,blank=True,null=True, verbose_name='Отлив ширина ( общая ) ')
    low_tides_length = models.IntegerField(default=0,blank=True,null=True, verbose_name='Отлив длинна ( общая ) ')
    low_tides_width_1 = models.IntegerField(default=0,blank=True,null=True, verbose_name='Отлив ширина 1')
    low_tides_width_2 = models.IntegerField(default=0,blank=True,null=True, verbose_name='Отлив ширина 2')
    low_tides_width_3 = models.IntegerField(default=0,blank=True,null=True, verbose_name='Отлив ширина 3')
    low_tides_width_4 = models.IntegerField(default=0,blank=True,null=True, verbose_name='Отлив ширина 4')

    lock_count = models.IntegerField(default=0,blank=True,null=True, verbose_name='Количество замком')

    length = models.FloatField(max_length=255, default=0.0, verbose_name='Длинна')
    count = models.FloatField(max_length=255, default=0.0, verbose_name='Количество')

    linear_meter = models.FloatField(max_length=255, default=0.0, verbose_name='В метрах погонных')
    square_meter = models.FloatField(max_length=255, default=0.0, verbose_name='В метрах квадратных')

    linear_meter_lock = models.FloatField(max_length=255, default=0.0, verbose_name='В метрах погонных (замок)')
    square_meter_lock = models.FloatField(max_length=255, default=0.0, verbose_name='В метрах квадратных (замок)')
    price_lock = models.FloatField(max_length=255, default=0.0, verbose_name='Цена замка')

    linear_meter_low_tides = models.FloatField(max_length=255, default=0.0, verbose_name='В метрах погонных (отлив)')
    square_meter_low_tides = models.FloatField(max_length=255, default=0.0, verbose_name='В метрах квадратных (отлив)')
    price_low_tides = models.FloatField(max_length=255, default=0.0, verbose_name='Цена отлива')


    price_output = models.FloatField(max_length=255, default=0.0, verbose_name='Цена')

    def __str__(self):
        return f' Откос из метлла № {self.pk} длинна {self.length} / ширина {self.width} = {self.price_output} BYN'

    class Meta:
        verbose_name = 'Просчет откосов из металла'
        verbose_name_plural = 'Просчеты откосов из металла'


class InternalSlopeInstallation(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название монтажа", blank=True, null=True)
    value = models.FloatField(default=0.0, verbose_name="Стоимость монтажа", blank=True, null=True)

    def __str__(self):
        return f' Монтаж {self.name} цена {self.value} BYN'

    class Meta:
        verbose_name = 'Монтаж внутренних откосов'
        verbose_name_plural = 'Монтажи внутренних откосов'


class InternalSlopeCalc(models.Model):
    internal_slope_id = models.IntegerField(default=0.0, verbose_name="№ Внутренние откосов", blank=True, null=True)

    installation_id = models.IntegerField(default=0, verbose_name='Установка', blank=True, null=True)
    color_id = models.IntegerField(default=0, verbose_name='Цвет', blank=True, null=True)

    markups_type = models.CharField(max_length=255, verbose_name='Наценка')
    width = models.FloatField(max_length=255, default=0.0, verbose_name='Ширина')
    count = models.FloatField(max_length=255, default=0.0, verbose_name='Количество')
    linear_meter = models.FloatField(max_length=255, default=0.0, verbose_name='В метрах погонных')
    square_meter = models.FloatField(max_length=255, default=0.0, verbose_name='В метрах квадратных')

    height_1 = models.IntegerField(default=0.0,blank=True,null=True, verbose_name='Высота 1')
    height_2 = models.IntegerField(default=0.0,blank=True,null=True, verbose_name='Высота 2')
    length = models.IntegerField(default=0.0,blank=True,null=True, verbose_name='Длинна')

    start_profile_length = models.IntegerField( default=0.0,blank=True,null=True, verbose_name='Стартовый профиль в мп')
    casing_length = models.IntegerField( default=0.0,blank=True,null=True, verbose_name='Наличник профиль в мп')
    lid_count = models.IntegerField(default=0.0,blank=True,null=True, verbose_name='Кол-во крышек')
    latch_count = models.IntegerField( default=0.0,blank=True,null=True, verbose_name='Кол-во защелок')
    f_count = models.IntegerField(default=0.0,blank=True,null=True, verbose_name='Кол-во F')

    price_output = models.FloatField(max_length=255, default=0.0, verbose_name='Цена')

    def __str__(self):
        return f' Внутренний откос № {self.pk} длинна {self.length} / ширина {self.width} = {self.price_output} BYN'

    class Meta:
        verbose_name = 'Просчет внутреннего откоса '
        verbose_name_plural = 'Просчеты внутренних откосов'


class MountingMaterialsCalc(models.Model):
    mounting_materials_id = models.IntegerField(default=0.0, verbose_name="№ Монтажного материала", blank=True,
                                                null=True)

    markups_type = models.CharField(max_length=255, verbose_name='Наценка ')
    count = models.FloatField(max_length=255, default=0.0, verbose_name='Количество')

    price_output = models.FloatField(max_length=255, default=0.0, verbose_name='Цена')

    def __str__(self):
        return f' Монтажные материалы № {self.pk} = {self.price_output} BYN'

    class Meta:
        verbose_name = 'Просчет монтажных материалов'
        verbose_name_plural = 'Просчеты монтажных материалов'


class WindowDiscountMarkups(models.Model):
    profile_id = models.ForeignKey(Profile, verbose_name="Профиль", blank=True, null=True, on_delete=models.CASCADE)
    fittings_id = models.ForeignKey(Fittings, verbose_name="Фурнитура", blank=True, null=True, on_delete=models.CASCADE)
    discount = models.FloatField(max_length=255, default=0.0, verbose_name='Значение скидки')

    markups_diler = models.FloatField(default=0.0, max_length=255, verbose_name='Наценка №1')
    markups_diler_in_percent = models.BooleanField(default=True, verbose_name='Добавлять в процентах ( наценка №1 )')

    markups_retail = models.FloatField(default=0.0, max_length=255, verbose_name='Наценка №2')
    markups_retail_in_percent = models.BooleanField(default=True, verbose_name='Добавлять в процентах ( наценка №2 )')

    markups_3 = models.FloatField(default=0.0, max_length=255, verbose_name='Наценка №3')
    markups_3_in_percent = models.BooleanField(default=True, verbose_name='Добавлять в процентах ( наценка №3 )')

    markups_4 = models.FloatField(default=0.0, max_length=255, verbose_name='Наценка №4')
    markups_4_in_percent = models.BooleanField(default=True, verbose_name='Добавлять в процентах ( наценка №4 )')

    markups_5 = models.FloatField(default=0.0, max_length=255, verbose_name='Наценка №5')
    markups_5_in_percent = models.BooleanField(default=True, verbose_name='Добавлять в процентах ( наценка №5 )')

    markups_6 = models.FloatField(default=0.0, max_length=255, verbose_name='Наценка №6')
    markups_6_in_percent = models.BooleanField(default=True, verbose_name='Добавлять в процентах ( наценка №6 )')

    markups_7 = models.FloatField(default=0.0, max_length=255, verbose_name='Наценка №7')
    markups_7_in_percent = models.BooleanField(default=True, verbose_name='Добавлять в процентах ( наценка №7 )')

    def __str__(self):
        return f'Профиль : {self.profile_id.name} + Фурнитура: скидка {self.fittings_id.name} = {self.discount} %,'

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

    markups_type = models.IntegerField(blank=True, null=True, verbose_name='Тип наценки')
    markups_name = models.CharField(max_length=255, blank=True, null=True, verbose_name='Название наценки')
    markups_value = models.FloatField(max_length=255, default=0.0, verbose_name='Значение наценки')
    markups_percent = models.BooleanField(default=True, verbose_name='Наценка в процентах')

    def __str__(self):
        return f' Просчет окна № {self.pk} на сумму {self.price_output} BYN'

    class Meta:
        verbose_name = 'Просчет окна'
        verbose_name_plural = 'Просчеты окон'


class Constructor(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, verbose_name="Автор",
                                     null=True, blank=True)
    name = models.CharField(max_length=255, verbose_name="Имя", blank=True, null=True)
    context = models.CharField(max_length=255, verbose_name="Контекст", blank=True, null=True)
    stb_info = models.CharField(max_length=255, verbose_name="СТБ название", blank=True, null=True)

    configuration = models.TextField(blank=True, null=True)
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
    sealant = models.ForeignKey(Sealant, on_delete=models.SET_NULL, verbose_name="Уплотнитель", null=True, blank=True)


    price_constructor = models.FloatField(default=0.0, verbose_name='Цена всего просчета', max_length=255, null=True,
                                          blank=True)
    # MATERIALS END
    window_calc = models.ForeignKey(WindowsCalc, on_delete=models.SET_NULL, verbose_name="Просчет окна", null=True,
                                    blank=True)
    other_complectation_profile_calc = models.ManyToManyField(OtherComplectationProfileCalc,
                                                              verbose_name="Прочее комплектующие",
                                                              blank=True)
    connection_profile_calc = models.ManyToManyField(ConnectionProfileCalc,
                                           verbose_name="Соединительные профиля",blank=True)
    additional_profile_calc = models.ManyToManyField(AdditionalProfileCalc,
                                           verbose_name="Доборные профиля", blank=True)

    windowsills_calc = models.ManyToManyField(WindowsillCalc, verbose_name="Просчеты подоконников", blank=True)
    lowtides_calc = models.ManyToManyField(LowTidesCalc, verbose_name="Просчеты отливов", blank=True)
    flashing_calc = models.ManyToManyField(FlashingCalc, verbose_name="Просчеты нащельников", blank=True)
    visors_calc = models.ManyToManyField(VisorsCalc, verbose_name="Просчеты козырьков", blank=True)
    casing_calc = models.ManyToManyField(CasingCalc, verbose_name="Просчеты наличников", blank=True)

    slopes_of_metal_calc = models.ManyToManyField(SlopesOfMetalCalc, verbose_name="Просчеты откосов из металла",
                                                  blank=True)
    internal_slope_calc = models.ManyToManyField(InternalSlopeCalc, verbose_name="Просчеты внутренних откосов",
                                                 blank=True)
    mounting_materials_calc = models.ManyToManyField(MountingMaterialsCalc, verbose_name="Просчеты монтажные материалы",
                                                     blank=True)
    works = models.ManyToManyField(Works, verbose_name='Работы', blank=True)

    final_image = models.TextField(max_length=10000000,verbose_name='Изображение', blank=True, null=True)
    final_image_url = models.CharField(max_length=255,verbose_name='Изображение url', blank=True, null=True)

    def __str__(self):
        return f'Просчет конструктора № {self.pk} на сумму {self.price_constructor}'

    class Meta:
        verbose_name = 'Просчет конструктора'
        verbose_name_plural = 'Просчеты конструкторов'

