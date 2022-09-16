from django.db import models


class Configuration(models.Model):
    product_type = models.CharField(max_length=255, verbose_name="Тип изделия")
    profile = models.CharField(max_length=255, verbose_name="Профиль")
    aggregate = models.CharField(max_length=255, verbose_name="Заполнитель №1")
    fittings = models.CharField(max_length=255, verbose_name="Фурнитура")
    seal_outside = models.CharField(max_length=255, verbose_name="Уплотнение снаружи")
    seal_rebate = models.CharField(max_length=255, verbose_name="Уплотнение притвора")
    seal_internal = models.CharField(max_length=255, verbose_name="Уплотнение внутренее")
    lock = models.CharField(max_length=255, verbose_name="Замок")
    shpros = models.CharField(max_length=255, verbose_name="Шпрос")
    shtapik = models.CharField(max_length=255, verbose_name="Шталик")
    sash = models.CharField(max_length=255, verbose_name="Створка")
    lamination_outside = models.CharField(max_length=255, verbose_name="Ламинация снаружи")
    lamination_inside = models.CharField(max_length=255, verbose_name="Ланиманция внутри")
    profile_weight = models.CharField(max_length=255, verbose_name="Масса профиля")
    note = models.CharField(max_length=255, verbose_name="Примечание")


class ExtraWork(models.Model):
    products_install = models.CharField(max_length=255, verbose_name="Монтаж изделий")
    pvc_slopes = models.CharField(max_length=255, verbose_name="Откосы ПВХ")
    free_positions = models.CharField(max_length=255, verbose_name="Бесплатные позиции")


class ExtraMaterial(models.Model):
    favorite_positions = models.CharField(max_length=255, verbose_name="Избранные позиции")
    windowsill = models.CharField(max_length=255, verbose_name="Подоконники")
    windowsill_danke_komfort = models.CharField(max_length=255, verbose_name="Подоконник Danke Komfort")
    windowsill_danke_standart = models.CharField(max_length=255, verbose_name="Подоконник Danke Standart")
    windowsill_danke_premium = models.CharField(max_length=255, verbose_name="Подоконник Danke Premium")
    low_tides = models.CharField(max_length=255, verbose_name="Отливы")
    visors = models.CharField(max_length=255, verbose_name="Козырьки")
    flashing = models.CharField(max_length=255, verbose_name="Нащельник")
    flashing_metal = models.CharField(max_length=255, verbose_name="Нащельник Металл")
    platband = models.CharField(max_length=255, verbose_name="Наличник")
    extensions_to_profile60 = models.CharField(max_length=255, verbose_name="Доборы к профилю 60мм")
    extensions_to_profile70 = models.CharField(max_length=255, verbose_name="Доборы к профилю 70мм")
    bay_window_to_profile60 = models.CharField(max_length=255, verbose_name="Эркер к профилю 60мм")
    bay_window_to_profile70 = models.CharField(max_length=255, verbose_name="Эркер к профилю 70мм")
    connector_90g = models.CharField(max_length=255, verbose_name="Соединитель 90гр")
    accessories = models.CharField(max_length=255, verbose_name="Комлпектующие")
    handles_and_locks = models.CharField(max_length=255, verbose_name="Ручки и замки")
    straight_connectors = models.CharField(max_length=255, verbose_name="Прямые соединители")
