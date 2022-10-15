from django.db import models
from constructor.models import *


# Create your models here.
class Constructor(models.Model):
    is_active = models.BooleanField(verbose_name="Активно", default=True)
    product_type = models.ForeignKey(ProductType, on_delete=models.SET_NULL, verbose_name="Тип изделия",
                                     null=True, blank=True)
    profile = models.ForeignKey(Profile, on_delete=models.SET_NULL, verbose_name="Профиль", null=True,
                                blank=True)
    aggregate = models.ForeignKey(Aggregate, on_delete=models.SET_NULL, verbose_name="Заполнитель №1",
                                  null=True, blank=True)
    fittings = models.ForeignKey(Fittings, on_delete=models.SET_NULL, verbose_name="Фурнитура",
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
    # windowsill_danke_komfort = models.ForeignKey(WindowsillDankeKomfort, on_delete=models.SET_NULL,
    #                                              verbose_name="Подоконник Danke Komfort", null=True, blank=True)
    # windowsill_danke_standart = models.ForeignKey(WindowsillDankeStandart, on_delete=models.SET_NULL,
    #                                               verbose_name="Подоконник Danke Standart", null=True, blank=True)
    # windowsill_danke_premium = models.ForeignKey(WindowsillDankePremium, on_delete=models.SET_NULL,
    #                                              verbose_name="Подоконник Danke Premium", null=True, blank=True)
    # low_tides = models.ForeignKey(LowTides, on_delete=models.SET_NULL, verbose_name="Отливы",
    #                               null=True, blank=True)
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
    currency = models.CharField(max_length=255, default='RUS', blank=True, null=True)
    price_window = models.FloatField(default=0.0, verbose_name='Цена окно ( с наценкой )', max_length=255, null=True,
                                     blank=True)
    price_works = models.FloatField(default=0.0, verbose_name='Цена работы', max_length=255, null=True, blank=True)
    price_material = models.FloatField(default=0.0, verbose_name='Цена материалов ( с наценкой )', max_length=255,
                                       null=True,
                                       blank=True)
    price_constructor = models.FloatField(default=0.0, verbose_name='Цена всего просчета', max_length=255, null=True,
                                          blank=True)

    def __str__(self):
        return f'Просчет №{self.id}'

    class Meta:
        verbose_name = 'Просчет'
        verbose_name_plural = 'Просчеты'
