from django.db import models
from django.forms import TextInput

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

    # price = models.FloatField(verbose_name="Цена", blank=True, null=True)
    # discount = models.FloatField(verbose_name="Скидка", blank=True, null=True)

    def __str__(self):
        return f'№ {self.id} имя : {self.name}'

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'


class Fittings(models.Model):
    name = models.CharField(max_length=255, verbose_name="Фурнитура", blank=True, null=True)

    # price = models.FloatField(verbose_name="Цена", blank=True, null=True)
    # discount = models.FloatField(verbose_name="Скидка", blank=True, null=True)

    def __str__(self):
        return f'№ {self.id} имя : {self.name}'

    class Meta:
        verbose_name = 'Фурнитура'
        verbose_name_plural = 'Фурнитуры'


class Aggregate(models.Model):
    name = models.CharField(max_length=255, verbose_name="Заполнитель №1", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Заполнитель №1'
        verbose_name_plural = 'Заполнитель №1'


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


class LaminationOutside(models.Model):
    name = models.CharField(max_length=255, verbose_name="Ламинация снаружи", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Ламинация снаружи'
        verbose_name_plural = 'Ламинация снаружи'


class LaminationInside(models.Model):
    name = models.CharField(max_length=255, verbose_name="Ланиманция внутри", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Ланиманция внутри'
        verbose_name_plural = 'Ланиманция внутри'


class ProfileWeight(models.Model):
    name = models.CharField(max_length=255, verbose_name="Масса профиля", blank=True, null=True)

    def __str__(self):
        return f'{self.id} {self.name}'

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


class ProductsInstall(models.Model):
    name = models.CharField(max_length=255, verbose_name="Монтаж изделий", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Монтаж изделий'
        verbose_name_plural = 'Монтаж изделий'


class PvcSlopes(models.Model):
    name = models.CharField(max_length=255, verbose_name="Откосы ПВХ", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Откосы ПВХ'
        verbose_name_plural = 'Откосы ПВХ'


class FreePositions(models.Model):
    name = models.CharField(max_length=255, verbose_name="Бесплатные позиции", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Бесплатные позиции'
        verbose_name_plural = 'Бесплатные позиции'


# _______________________________ EXTRAMATERIAL MODEL _______________________________
class WindowsillType(models.Model):
    name = models.CharField(max_length=255, verbose_name='Тип подоконника', blank=True, null=True)
    type_name = models.CharField(max_length=255, verbose_name='windowsill_type', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тип подоконника'
        verbose_name_plural = 'Тип подоконников'


class WindowsillColor(models.Model):
    name = models.CharField(max_length=255, verbose_name='Цвет подоконника', blank=True, null=True)

    def __str__(self):
        return f' {self.name}'

    class Meta:
        verbose_name = 'Цвет подоконника'
        verbose_name_plural = 'Цвета подоконников'


class Windowsill(models.Model):
    color = models.ForeignKey(WindowsillColor, on_delete=models.CASCADE, blank=True, verbose_name='Цвет подоконника')
    type = models.ForeignKey(WindowsillType, on_delete=models.CASCADE, blank=True, verbose_name='Тип подоконника')
    price_input = models.FloatField(default=0.0, verbose_name='Цена закупки', blank=True, null=True)

    def __str__(self):
        return f'# {self.id} цвет: {self.color}, тип: {self.type}, цена закупки: {self.price_input}'

    class Meta:
        verbose_name = 'Подоконник'
        verbose_name_plural = 'Подоконники'


class LowTidesType(models.Model):
    name = models.CharField(max_length=255, verbose_name="Тип отлива", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тип отлива'
        verbose_name_plural = 'Типы отливов'


class LowTides(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название отлива", blank=True, null=True)
    type = models.ForeignKey(LowTidesType, on_delete=models.CASCADE, blank=True, verbose_name='Тип отлива')
    price_input = models.FloatField(default=0.0, verbose_name='Цена закупки', blank=True, null=True)

    def __str__(self):
        return f'{self.id} {self.name}'

    class Meta:
        verbose_name = 'Отлив'
        verbose_name_plural = 'Отливы'


class FavoritePositions(models.Model):
    name = models.CharField(max_length=255, verbose_name="Избранные позиции", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Избранные позиции'
        verbose_name_plural = 'Избранные позиции'


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


class FlashingMetal(models.Model):
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


class ExtensionsToProfile60(models.Model):
    name = models.CharField(max_length=255, verbose_name="Доборы к профилю 60мм", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Доборы к профилю 60мм'
        verbose_name_plural = 'Доборы к профилю 60мм'


class ExtensionsToProfile70(models.Model):
    name = models.CharField(max_length=255, verbose_name="Доборы к профилю 70мм", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Доборы к профилю 70мм'
        verbose_name_plural = 'Доборы к профилю 70мм'


class BayWindowToProfile60(models.Model):
    name = models.CharField(max_length=255, verbose_name="Эркер к профилю 60мм", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Эркер к профилю 60мм'
        verbose_name_plural = 'Эркер к профилю 60мм'


class BayWindowToProfile70(models.Model):
    name = models.CharField(max_length=255, verbose_name="Эркер к профилю 70мм", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Эркер к профилю 70мм'
        verbose_name_plural = 'Эркер к профилю 70мм'


class Connector90g(models.Model):
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


class StraightConnectors(models.Model):
    name = models.CharField(max_length=255, verbose_name="Прямые соединители", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Прямые соединители'
        verbose_name_plural = 'Прямые соединители'


class SupplyValve(models.Model):
    name = models.CharField(max_length=255, verbose_name="Приточный клапан", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Приточный клапан'
        verbose_name_plural = 'Приточные клапаны'


class Works(models.Model):
    name = models.CharField(max_length=255, verbose_name='Наименование работы', blank=True, null=True)
    price = models.FloatField(max_length=255, default=0.0, verbose_name='Цена работы')

    def __str__(self):
        return f' Работы № {self.id} {self.name} на сумму {self.price} BYN'

    class Meta:
        verbose_name = 'Просчет работы'
        verbose_name_plural = 'Просчеты работ'
