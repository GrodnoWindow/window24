from django.db import models


# _______________________________ PRICE MODEL _______________________________
class Price(models.Model):
    price = models.FloatField(verbose_name="Цена", blank=True)
    discount = models.IntegerField(verbose_name="Скидка", blank=True)

    def __str__(self):
        return 'Цена - %s, скидка - %s' % (self.price, self.discount)

    class Meta:
        verbose_name = 'Цена'
        verbose_name_plural = 'Цены'


# _______________________________ CONFIGURATION MODEL _______________________________
class ProductType(models.Model):
    product_type_name = models.CharField(max_length=255, verbose_name="Тип изделия", blank=True)

    def __str__(self):
        return self.product_type_name

    class Meta:
        verbose_name = 'Тип изделия'
        verbose_name_plural = 'Тип изделия'


class Profile(models.Model):
    profile_name = models.CharField(max_length=255, verbose_name="Профиль", blank=True)
    price = models.ManyToManyField(Price)

    def __str__(self):
        return self.profile_name

    def get_price(self):
        return ",".join([str(f) for f in self.price.all()])

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'


class Aggregate(models.Model):
    aggregate = models.CharField(max_length=255, verbose_name="Заполнитель №1", blank=True)

    def __str__(self):
        return self.aggregate

    class Meta:
        verbose_name = 'Заполнитель №1'
        verbose_name_plural = 'Заполнитель №1'


class Fittings(models.Model):
    fittings = models.CharField(max_length=255, verbose_name="Фурнитура", blank=True)
    price = models.ManyToManyField(Price)

    def __str__(self):
        return self.fittings

    def get_price(self):
        return ",".join([str(f) for f in self.price.all()])

    class Meta:
        verbose_name = 'Фурнитура'
        verbose_name_plural = 'Фурнитуры'


class SealOutside(models.Model):
    seal_outside = models.CharField(max_length=255, verbose_name="Уплотнение снаружи", blank=True)

    def __str__(self):
        return self.seal_outside

    class Meta:
        verbose_name = 'Уплотнение снаружи'
        verbose_name_plural = 'Уплотнение снаружи'


class SealRebate(models.Model):
    seal_rebate = models.CharField(max_length=255, verbose_name="Уплотнение притвора", blank=True)

    def __str__(self):
        return self.seal_rebate

    class Meta:
        verbose_name = 'Уплотнение притвора'
        verbose_name_plural = 'Уплотнение притвора'


class SealInternal(models.Model):
    seal_internal = models.CharField(max_length=255, verbose_name="Уплотнение внутренее", blank=True)

    def __str__(self):
        return self.seal_internal

    class Meta:
        verbose_name = 'Уплотнение внутренее'
        verbose_name_plural = 'Уплотнение внутренее'


class Lock(models.Model):
    lock_name = models.CharField(max_length=255, verbose_name="Замок", blank=True)

    def __str__(self):
        return self.lock_name

    class Meta:
        verbose_name = 'Замок'
        verbose_name_plural = 'Замки'


class Shpros(models.Model):
    shpros_name = models.CharField(max_length=255, verbose_name="Шпрос", blank=True)

    def __str__(self):
        return self.shpros_name

    class Meta:
        verbose_name = 'Шпрос'
        verbose_name_plural = 'Шпросы'


class Shtapik(models.Model):
    shtapik = models.CharField(max_length=255, verbose_name="Штапик", blank=True)

    def __str__(self):
        return self.shtapik

    class Meta:
        verbose_name = 'Штапик'
        verbose_name_plural = 'Штапики'


class Sash(models.Model):
    sash = models.CharField(max_length=255, verbose_name="Створка", blank=True)

    def __str__(self):
        return self.sash

    class Meta:
        verbose_name = 'Створка'
        verbose_name_plural = 'Створки'


class Lamination_outside(models.Model):
    lamination_outside = models.CharField(max_length=255, verbose_name="Ламинация снаружи", blank=True)

    def __str__(self):
        return self.lamination_outside

    class Meta:
        verbose_name = 'Ламинация снаружи'
        verbose_name_plural = 'Ламинация снаружи'


class Lamination_inside(models.Model):
    lamination_inside = models.CharField(max_length=255, verbose_name="Ланиманция внутри", blank=True)

    def __str__(self):
        return self.lamination_inside

    class Meta:
        verbose_name = 'Ланиманция внутри'
        verbose_name_plural = 'Ланиманция внутри'


class Profile_weight(models.Model):
    profile_weight = models.CharField(max_length=255, verbose_name="Масса профиля", blank=True)

    def __str__(self):
        return self.profile_weight

    class Meta:
        verbose_name = 'Масса профиля'
        verbose_name_plural = 'Масса профиля'


class Note(models.Model):
    note = models.CharField(max_length=255, verbose_name="Примечание", blank=True)

    def __str__(self):
        return self.note

    class Meta:
        verbose_name = 'Примечание'
        verbose_name_plural = 'Примечание'


# _______________________________ EXTRAWORK MODEL _______________________________


class Products_install(models.Model):
    products_install = models.CharField(max_length=255, verbose_name="Монтаж изделий", blank=True)

    def __str__(self):
        return self.products_install

    class Meta:
        verbose_name = 'Монтаж изделий'
        verbose_name_plural = 'Монтаж изделий'


class Pvc_slopes(models.Model):
    pvc_slopes = models.CharField(max_length=255, verbose_name="Откосы ПВХ", blank=True)

    def __str__(self):
        return self.pvc_slopes

    class Meta:
        verbose_name = 'Откосы ПВХ'
        verbose_name_plural = 'Откосы ПВХ'


class Free_positions(models.Model):
    free_positions = models.CharField(max_length=255, verbose_name="Бесплатные позиции", blank=True)

    def __str__(self):
        return self.free_positions

    class Meta:
        verbose_name = 'Бесплатные позиции'
        verbose_name_plural = 'Бесплатные позиции'


# _______________________________ EXTRAMATERIAL MODEL _______________________________
class Favorite_positions(models.Model):
    favorite_positions = models.CharField(max_length=255, verbose_name="Избранные позиции", blank=True)

    def __str__(self):
        return self.favorite_positions

    class Meta:
        verbose_name = 'Избранные позиции'
        verbose_name_plural = 'Избранные позиции'


class Windowsill(models.Model):
    windowsill = models.CharField(max_length=255, verbose_name="Подоконники", blank=True)

    def __str__(self):
        return self.windowsill

    class Meta:
        verbose_name = 'Подоконники'
        verbose_name_plural = 'Подоконники'


class Windowsill_danke_komfort(models.Model):
    windowsill_danke_komfort = models.CharField(max_length=255, verbose_name="Подоконник Danke Komfort", blank=True)

    def __str__(self):
        return self.windowsill_danke_komfort

    class Meta:
        verbose_name = 'Подоконник Danke Komfort'
        verbose_name_plural = 'Подоконник Danke Komfort'


class Windowsill_danke_standart(models.Model):
    windowsill_danke_standart = models.CharField(max_length=255, verbose_name="Подоконник Danke Standart", blank=True)

    def __str__(self):
        return self.windowsill_danke_standart

    class Meta:
        verbose_name = 'Подоконник Danke Standart'
        verbose_name_plural = 'Подоконник Danke Standart'


class Windowsill_danke_premium(models.Model):
    windowsill_danke_premium = models.CharField(max_length=255, verbose_name="Подоконник Danke Premium", blank=True)

    def __str__(self):
        return self.windowsill_danke_premium

    class Meta:
        verbose_name = 'Подоконник Danke Premium'
        verbose_name_plural = 'Подоконник Danke Premium'


class Low_tides(models.Model):
    low_tides = models.CharField(max_length=255, verbose_name="Отливы", blank=True)

    def __str__(self):
        return self.low_tides

    class Meta:
        verbose_name = 'Отливы'
        verbose_name_plural = 'Отливы'


class Visors(models.Model):
    visors = models.CharField(max_length=255, verbose_name="Козырьки", blank=True)

    def __str__(self):
        return self.visors

    class Meta:
        verbose_name = 'Козырьки'
        verbose_name_plural = 'Козырьки'


class Flashing(models.Model):
    flashing = models.CharField(max_length=255, verbose_name="Нащельник", blank=True)

    def __str__(self):
        return self.flashing

    class Meta:
        verbose_name = 'Нащельник'
        verbose_name_plural = 'Нащельник'


class Flashing_metal(models.Model):
    flashing_metal = models.CharField(max_length=255, verbose_name="Нащельник Металл", blank=True)

    def __str__(self):
        return self.flashing_metal

    class Meta:
        verbose_name = 'Нащельник Металл'
        verbose_name_plural = 'Нащельник Металл'


class Platband(models.Model):
    platband = models.CharField(max_length=255, verbose_name="Наличник", blank=True)

    def __str__(self):
        return self.platband

    class Meta:
        verbose_name = 'Наличник'
        verbose_name_plural = 'Наличник'


class Extensions_to_profile_sixty(models.Model):
    extensions_to_profile_sixty = models.CharField(max_length=255, verbose_name="Доборы к профилю 60мм", blank=True)

    def __str__(self):
        return self.extensions_to_profile_sixty

    class Meta:
        verbose_name = 'Доборы к профилю 60мм'
        verbose_name_plural = 'Доборы к профилю 60мм'


class Extensions_to_profile_seventy(models.Model):
    extensions_to_profile_seventy = models.CharField(max_length=255, verbose_name="Доборы к профилю 70мм", blank=True)

    def __str__(self):
        return self.extensions_to_profile_seventy

    class Meta:
        verbose_name = 'Доборы к профилю 70мм'
        verbose_name_plural = 'Доборы к профилю 70мм'


class Bay_window_to_profile_sixty(models.Model):
    bay_window_to_profile_sixty = models.CharField(max_length=255, verbose_name="Эркер к профилю 60мм", blank=True)

    def __str__(self):
        return self.bay_window_to_profile_sixty

    class Meta:
        verbose_name = 'Эркер к профилю 60мм'
        verbose_name_plural = 'Эркер к профилю 60мм'


class Bay_window_to_profile_seventy(models.Model):
    bay_window_to_profile_seventy = models.CharField(max_length=255, verbose_name="Эркер к профилю 70мм", blank=True)

    def __str__(self):
        return self.bay_window_to_profile_seventy

    class Meta:
        verbose_name = 'Эркер к профилю 70мм'
        verbose_name_plural = 'Эркер к профилю 70мм'


class Connector_90g(models.Model):
    connector_90g = models.CharField(max_length=255, verbose_name="Соединитель 90гр", blank=True)

    def __str__(self):
        return self.connector_90g

    class Meta:
        verbose_name = 'Соединитель 90гр'
        verbose_name_plural = 'Соединитель 90гр'


class Accessories(models.Model):
    accessories = models.CharField(max_length=255, verbose_name="Комлпектующие", blank=True)

    def __str__(self):
        return self.accessories

    class Meta:
        verbose_name = 'Комлпектующие'
        verbose_name_plural = 'Комлпектующие'


class Handles_and_locks(models.Model):
    handles_and_locks = models.CharField(max_length=255, verbose_name="Ручки и замки", blank=True)

    def __str__(self):
        return self.handles_and_locks

    class Meta:
        verbose_name = 'Ручки и замки'
        verbose_name_plural = 'Ручки и замки'


class Straight_connectors(models.Model):
    straight_connectors = models.CharField(max_length=255, verbose_name="Прямые соединители", blank=True)

    def __str__(self):
        return self.straight_connectors

    class Meta:
        verbose_name = 'Прямые соединители'
        verbose_name_plural = 'Прямые соединители'
