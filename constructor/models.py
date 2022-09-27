from django.db import models


# _______________________________ PRICE MODEL _______________________________
class Price(models.Model):
    price = models.FloatField(verbose_name="Цена", blank=True, null=True)
    discount = models.IntegerField(verbose_name="Скидка", blank=True, null=True)

    def __str__(self):
        return 'Цена - %s, скидка - %s' % (self.price, self.discount)

    class Meta:
        verbose_name = 'Цена'
        verbose_name_plural = 'Цены'


# _______________________________ CONFIGURATION MODEL _______________________________
class ProductType(models.Model):
    name = models.CharField(max_length=255, verbose_name="Тип изделия", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тип изделия'
        verbose_name_plural = 'Тип изделия'


class Profile(models.Model):
    name = models.CharField(max_length=255, verbose_name="Профиль", blank=True, null=True)
    price = models.ManyToManyField(Price)

    def __str__(self):
        return self.name

    def get_price(self):
        return ",".join([str(f) for f in self.price.all()])

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'


class Aggregate(models.Model):
    name = models.CharField(max_length=255, verbose_name="Заполнитель №1", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Заполнитель №1'
        verbose_name_plural = 'Заполнитель №1'


class Fittings(models.Model):
    name = models.CharField(max_length=255, verbose_name="Фурнитура", blank=True, null=True)
    price = models.ManyToManyField(Price)

    def __str__(self):
        return self.name

    def get_price(self):
        return ",".join([str(f) for f in self.price.all()])

    class Meta:
        verbose_name = 'Фурнитура'
        verbose_name_plural = 'Фурнитуры'


class SealOutside(models.Model):
    name = models.CharField(max_length=255, verbose_name="Уплотнение снаружи", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Уплотнение снаружи'
        verbose_name_plural = 'Уплотнение снаружи'


class SealRebate(models.Model):
    name = models.CharField(max_length=255, verbose_name="Уплотнение притвора", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Уплотнение притвора'
        verbose_name_plural = 'Уплотнение притвора'


class SealInternal(models.Model):
    name = models.CharField(max_length=255, verbose_name="Уплотнение внутренее", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Уплотнение внутренее'
        verbose_name_plural = 'Уплотнение внутренее'


class SealColor(models.Model):
    name = models.CharField(max_length=255, verbose_name="Цвет уплотнения", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Цвет уплотнения'
        verbose_name_plural = 'Цвет уплотнения'


class Shpros(models.Model):
    name = models.CharField(max_length=255, verbose_name="Шпрос", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Шпрос'
        verbose_name_plural = 'Шпросы'


class Shtapik(models.Model):
    name = models.CharField(max_length=255, verbose_name="Штапик", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Штапик'
        verbose_name_plural = 'Штапики'


class Sash(models.Model):
    name = models.CharField(max_length=255, verbose_name="Створка", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Створка'
        verbose_name_plural = 'Створки'


class Lamination_outside(models.Model):
    name = models.CharField(max_length=255, verbose_name="Ламинация снаружи", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Ламинация снаружи'
        verbose_name_plural = 'Ламинация снаружи'


class Lamination_inside(models.Model):
    name = models.CharField(max_length=255, verbose_name="Ланиманция внутри", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Ланиманция внутри'
        verbose_name_plural = 'Ланиманция внутри'


class Profile_weight(models.Model):
    name = models.CharField(max_length=255, verbose_name="Масса профиля", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Масса профиля'
        verbose_name_plural = 'Масса профиля'


class Note(models.Model):
    name = models.CharField(max_length=255, verbose_name="Примечание", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Примечание'
        verbose_name_plural = 'Примечание'


# _______________________________ EXTRAWORK MODEL _______________________________


class Products_install(models.Model):
    name = models.CharField(max_length=255, verbose_name="Монтаж изделий", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Монтаж изделий'
        verbose_name_plural = 'Монтаж изделий'


class Pvc_slopes(models.Model):
    name = models.CharField(max_length=255, verbose_name="Откосы ПВХ", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Откосы ПВХ'
        verbose_name_plural = 'Откосы ПВХ'


class Free_positions(models.Model):
    name = models.CharField(max_length=255, verbose_name="Бесплатные позиции", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Бесплатные позиции'
        verbose_name_plural = 'Бесплатные позиции'


# _______________________________ EXTRAMATERIAL MODEL _______________________________
class Favorite_positions(models.Model):
    name = models.CharField(max_length=255, verbose_name="Избранные позиции", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Избранные позиции'
        verbose_name_plural = 'Избранные позиции'


class Windowsill(models.Model):
    name = models.CharField(max_length=255, verbose_name="Подоконники", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Подоконники'
        verbose_name_plural = 'Подоконники'


class Windowsill_danke_komfort(models.Model):
    name = models.CharField(max_length=255, verbose_name="Подоконник Danke Komfort", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Подоконник Danke Komfort'
        verbose_name_plural = 'Подоконник Danke Komfort'


class Windowsill_danke_standart(models.Model):
    name = models.CharField(max_length=255, verbose_name="Подоконник Danke Standart", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Подоконник Danke Standart'
        verbose_name_plural = 'Подоконник Danke Standart'


class Windowsill_danke_premium(models.Model):
    name = models.CharField(max_length=255, verbose_name="Подоконник Danke Premium", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Подоконник Danke Premium'
        verbose_name_plural = 'Подоконник Danke Premium'


class Low_tides(models.Model):
    name = models.CharField(max_length=255, verbose_name="Отливы", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Отливы'
        verbose_name_plural = 'Отливы'


class Visors(models.Model):
    name = models.CharField(max_length=255, verbose_name="Козырьки", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Козырьки'
        verbose_name_plural = 'Козырьки'


class Flashing(models.Model):
    name = models.CharField(max_length=255, verbose_name="Нащельник", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Нащельник'
        verbose_name_plural = 'Нащельник'


class Flashing_metal(models.Model):
    name = models.CharField(max_length=255, verbose_name="Нащельник Металл", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Нащельник Металл'
        verbose_name_plural = 'Нащельник Металл'


class Platband(models.Model):
    name = models.CharField(max_length=255, verbose_name="Наличник", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Наличник'
        verbose_name_plural = 'Наличник'


class Extensions_to_profile_sixty(models.Model):
    name = models.CharField(max_length=255, verbose_name="Доборы к профилю 60мм", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Доборы к профилю 60мм'
        verbose_name_plural = 'Доборы к профилю 60мм'


class Extensions_to_profile_seventy(models.Model):
    name = models.CharField(max_length=255, verbose_name="Доборы к профилю 70мм", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Доборы к профилю 70мм'
        verbose_name_plural = 'Доборы к профилю 70мм'


class Bay_window_to_profile_sixty(models.Model):
    name = models.CharField(max_length=255, verbose_name="Эркер к профилю 60мм", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Эркер к профилю 60мм'
        verbose_name_plural = 'Эркер к профилю 60мм'


class Bay_window_to_profile_seventy(models.Model):
    name = models.CharField(max_length=255, verbose_name="Эркер к профилю 70мм", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Эркер к профилю 70мм'
        verbose_name_plural = 'Эркер к профилю 70мм'


class Connector_90g(models.Model):
    name = models.CharField(max_length=255, verbose_name="Соединитель 90гр", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Соединитель 90гр'
        verbose_name_plural = 'Соединитель 90гр'


class Accessories(models.Model):
    name = models.CharField(max_length=255, verbose_name="Комлпектующие", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Комлпектующие'
        verbose_name_plural = 'Комлпектующие'


class Handles(models.Model):
    name = models.CharField(max_length=255, verbose_name="Ручка", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Ручка'
        verbose_name_plural = 'Ручки'


class Locks(models.Model):
    name = models.CharField(max_length=255, verbose_name="Замок", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Замок'
        verbose_name_plural = 'Замки'


class Straight_connectors(models.Model):
    name = models.CharField(max_length=255, verbose_name="Прямые соединители", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Прямые соединители'
        verbose_name_plural = 'Прямые соединители'


class Supply_valve(models.Model):
    name = models.CharField(max_length=255, verbose_name="Приточный клапан", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Приточный клапан'
        verbose_name_plural = 'Приточные клапаны'


# _______________________________ CONSTRUCTOR MODEL _______________________________
class Constructor(models.Model):
    is_active = models.BooleanField(verbose_name="Активно", default=True)
    price = models.ForeignKey(Price, on_delete=models.SET_NULL, verbose_name="Цена", null=True,
                              blank=True)
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
    lamination_outside = models.ForeignKey(Lamination_outside, on_delete=models.SET_NULL,
                                           verbose_name="Ламинация снаружи", null=True, blank=True)
    lamination_inside = models.ForeignKey(Lamination_inside, on_delete=models.SET_NULL,
                                          verbose_name="Ланиманция внутри", null=True, blank=True)
    profile_weight = models.ForeignKey(Profile_weight, on_delete=models.SET_NULL,
                                       verbose_name="Масса профиля", null=True, blank=True)
    note = models.ForeignKey(Note, on_delete=models.SET_NULL, verbose_name="Примечание", null=True,
                             blank=True)
    products_install = models.ForeignKey(Products_install, on_delete=models.SET_NULL,
                                         verbose_name="Монтаж изделий", null=True, blank=True)
    pvc_slopes = models.ForeignKey(Pvc_slopes, on_delete=models.SET_NULL, verbose_name="Откосы ПВХ",
                                   null=True, blank=True)
    free_positions = models.ForeignKey(Free_positions, on_delete=models.SET_NULL,
                                       verbose_name="Бесплатные позиции", null=True, blank=True)
    favorite_positions = models.ForeignKey(Favorite_positions, on_delete=models.SET_NULL,
                                           verbose_name="Избранные позиции", null=True, blank=True)
    windowsill = models.ForeignKey(Windowsill, on_delete=models.SET_NULL, verbose_name="Подоконники",
                                   null=True, blank=True)
    windowsill_danke_komfort = models.ForeignKey(Windowsill_danke_komfort, on_delete=models.SET_NULL,
                                                 verbose_name="Подоконник Danke Komfort", null=True, blank=True)
    windowsill_danke_standart = models.ForeignKey(Windowsill_danke_standart, on_delete=models.SET_NULL,
                                                  verbose_name="Подоконник Danke Standart", null=True, blank=True)
    windowsill_danke_premium = models.ForeignKey(Windowsill_danke_premium, on_delete=models.SET_NULL,
                                                 verbose_name="Подоконник Danke Premium", null=True, blank=True)
    low_tides = models.ForeignKey(Low_tides, on_delete=models.SET_NULL, verbose_name="Отливы",
                                  null=True, blank=True)
    visors = models.ForeignKey(Visors, on_delete=models.SET_NULL, verbose_name="Козырьки", null=True,
                               blank=True)
    flashing = models.ForeignKey(Flashing, on_delete=models.SET_NULL, verbose_name="Нащельник",
                                 null=True, blank=True)
    flashing_metal = models.ForeignKey(Flashing_metal, on_delete=models.SET_NULL,
                                       verbose_name="Нащельник Металл", null=True, blank=True)
    platband = models.ForeignKey(Platband, on_delete=models.SET_NULL, verbose_name="Наличник",
                                 null=True, blank=True)
    extensions_to_profile60 = models.ForeignKey(Extensions_to_profile_sixty, on_delete=models.SET_NULL,
                                                verbose_name="Доборы к профилю 60мм", null=True, blank=True)
    extensions_to_profile70 = models.ForeignKey(Extensions_to_profile_seventy,
                                                on_delete=models.SET_NULL,
                                                verbose_name="Доборы к профилю 70мм", null=True, blank=True)
    bay_window_to_profile60 = models.ForeignKey(Bay_window_to_profile_sixty, on_delete=models.SET_NULL,
                                                verbose_name="Эркер к профилю 60мм", null=True, blank=True)
    bay_window_to_profile70 = models.ForeignKey(Bay_window_to_profile_seventy,
                                                on_delete=models.SET_NULL,
                                                verbose_name="Эркер к профилю 70мм", null=True, blank=True)
    connector_90g = models.ForeignKey(Connector_90g, on_delete=models.SET_NULL,
                                      verbose_name="Соединитель 90гр", null=True, blank=True)
    accessories = models.ForeignKey(Accessories, on_delete=models.SET_NULL,
                                    verbose_name="Комлпектующие", null=True, blank=True)
    handles = models.ForeignKey(Handles, on_delete=models.SET_NULL,
                                verbose_name="Ручка", null=True, blank=True)
    locks = models.ForeignKey(Locks, on_delete=models.SET_NULL,
                              verbose_name="Замок", null=True, blank=True)
    straight_connectors = models.ForeignKey(Straight_connectors, on_delete=models.SET_NULL,
                                            verbose_name="Прямые соединители", null=True, blank=True)
    supply_valve = models.ForeignKey(Supply_valve, on_delete=models.SET_NULL,
                                     verbose_name="Приточный клапан", null=True, blank=True)

    def __str__(self):
        return 'Конструктор'

    class Meta:
        verbose_name = 'Конструктор'
        verbose_name_plural = 'Конструктор'
