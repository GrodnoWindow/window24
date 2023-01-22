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
        return f'№ {self.pk} имя : {self.name}'

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'


class ProductTypeDoor(models.Model):
    name = models.CharField(max_length=255, verbose_name="Тип изделия", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тип изделия'
        verbose_name_plural = 'Тип изделия'


class Opening(models.Model):
    name = models.CharField(max_length=255, verbose_name="Открывание", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Открывание'
        verbose_name_plural = 'Открывания'


class Lock(models.Model):
    name = models.CharField(max_length=255, verbose_name="Дверной замок", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Дверной замок'
        verbose_name_plural = 'Дверные замки'


class DoorHandles(models.Model):
    name = models.CharField(max_length=255, verbose_name="Дверная ручки", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Дверная ручка'
        verbose_name_plural = 'Дверные ручки'


class DoorHinges(models.Model):
    name = models.CharField(max_length=255, verbose_name="Дверные петли", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Дверные петли'
        verbose_name_plural = 'Дверные петли'


class Cylinder(models.Model):
    name = models.CharField(max_length=255, verbose_name="Цилиндр", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Цилиндр'
        verbose_name_plural = 'Цилиндры'


class DoorCloser(models.Model):
    name = models.CharField(max_length=255, verbose_name="Доводчик", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Доводчик'
        verbose_name_plural = 'Доводчики'


class OpeningLimiter(models.Model):
    name = models.CharField(max_length=255, verbose_name="Ограничитель открывания", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Ограничитель открывания'
        verbose_name_plural = 'Ограничители открывания'


class Door(models.Model):
    product_type = models.ForeignKey(ProductTypeDoor, on_delete=models.SET_NULL, verbose_name="Тип изделия", blank=True,
                                     null=True)
    shtulp = models.BooleanField(default=False, verbose_name='Со штульпом', blank=True)
    opening = models.ForeignKey(Opening, on_delete=models.SET_NULL, verbose_name="Открывание", blank=True, null=True)
    lock = models.ForeignKey(Lock, on_delete=models.SET_NULL, verbose_name="Замок", blank=True, null=True)
    handle = models.ForeignKey(DoorHandles, on_delete=models.SET_NULL, verbose_name="Дверные ручки", blank=True,
                               null=True)
    door_hinges = models.ForeignKey(DoorHinges, on_delete=models.SET_NULL, verbose_name="Дверные петли", blank=True,
                                    null=True)
    cylinder = models.ForeignKey(Cylinder, on_delete=models.SET_NULL, verbose_name="Цилиндр", blank=True, null=True)
    door_closer = models.ForeignKey(DoorCloser, on_delete=models.SET_NULL, verbose_name="Доводчик", blank=True,
                                    null=True)
    opening_limiter = models.ForeignKey(OpeningLimiter, on_delete=models.SET_NULL,
                                        verbose_name="Ограничитель открывания", blank=True, null=True)

    def __str__(self):
        return f'№ {self.pk} {self.product_type}'

    class Meta:
        verbose_name = 'Дверь'
        verbose_name_plural = 'Двери'


class Article(models.Model):
    name = models.CharField(max_length=255, verbose_name="Артикуль", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Артикуль'
        verbose_name_plural = 'Артикули'


class ConnectionProfileName(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название соед.профиля", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Название соед.профиля'
        verbose_name_plural = 'Название соед.профиля'


class ColorInside(models.Model):
    name = models.CharField(max_length=255, verbose_name="Цвет внутри", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Цвет внутри'
        verbose_name_plural = 'Цвета внутри'


class ColorOutside(models.Model):
    name = models.CharField(max_length=255, verbose_name="Цвет снаружи", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Цвет снаружи'
        verbose_name_plural = 'Цвета снаружи'


class ConnectionProfile(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.SET_NULL, verbose_name="Профиль", blank=True, null=True)
    article = models.ForeignKey(Article, on_delete=models.SET_NULL, verbose_name="Артикуль", blank=True, null=True)
    name = models.ForeignKey(ConnectionProfileName, on_delete=models.SET_NULL, verbose_name="Название соен.профиля",
                             blank=True, null=True)
    color_inside = models.ForeignKey(ColorInside, on_delete=models.SET_NULL, verbose_name="Цвет внутри", blank=True,
                                     null=True)
    color_outside = models.ForeignKey(ColorOutside, on_delete=models.SET_NULL, verbose_name="Цвет снаружи", blank=True,
                                      null=True)
    length = models.FloatField(default=0.0, verbose_name="Длина", blank=True, null=True)
    price = models.FloatField(default=0.0, verbose_name="Цена", blank=True, null=True)

    def __str__(self):
        return f'№ {self.pk} {self.name}'

    class Meta:
        verbose_name = 'Соединительные профиля'
        verbose_name_plural = 'Соединительные профиля'


class ArticleAdditionalProfile(models.Model):
    name = models.CharField(max_length=255, verbose_name="Артикуль", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Артикуль доб. профиля'
        verbose_name_plural = 'Артикуль доб. профиля'


class AdditionalProfile(models.Model):
    article = models.ForeignKey(ArticleAdditionalProfile, on_delete=models.SET_NULL, verbose_name="Артикуль",
                                blank=True, null=True)
    width = models.FloatField(default=0.0, verbose_name="Ширина", blank=True, null=True)
    price = models.FloatField(default=0.0, verbose_name="Цена", blank=True, null=True)

    def __str__(self):
        return f'№ {self.pk} {self.article}'

    class Meta:
        verbose_name = 'Доборный профиль'
        verbose_name_plural = 'Доборные профиля'

class SealantColor(models.Model):
    name = models.CharField(max_length=255, verbose_name="Цвет уплотнения", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Цвет уплотнения'
        verbose_name_plural = 'Цвет уплотнения'



class SealantOutside(models.Model):
    name = models.CharField(max_length=255, verbose_name="Исполнение снаружи", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Исполнение снаружи уплотнителя'
        verbose_name_plural = 'Исполнение снаружи уплотнителя'


class SealantInside(models.Model):
    name = models.CharField(max_length=255, verbose_name="Исполнение внутри", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Исполнение внутри уплотнителя'
        verbose_name_plural = 'Исполнение внутрии уплотнителя'


class SealantShtapik(models.Model):
    name = models.CharField(max_length=255, verbose_name="Штапик", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Уплотнитель ( штапик )'
        verbose_name_plural = 'Уплотнитель ( штапики )'


class Sealant(models.Model):
    sealant_color = models.ForeignKey(SealantColor, on_delete=models.SET_NULL, verbose_name="Цвет уплотнителя", blank=True, null=True)
    sealant_inside = models.ForeignKey(SealantInside, on_delete=models.SET_NULL, verbose_name="Исполнение снаружи",
                                       blank=True, null=True)
    sealant_outside = models.ForeignKey(SealantOutside, on_delete=models.SET_NULL, verbose_name="Исполнение внутри",
                                        blank=True, null=True)
    sealant_shtapik = models.ForeignKey(SealantShtapik, on_delete=models.SET_NULL, verbose_name="Штапик",
                                        blank=True, null=True)

    def __str__(self):
        return f'№ {self.pk} {self.color}'

    class Meta:
        verbose_name = 'Уплотнитель'
        verbose_name_plural = 'Уплотнители'


class TypeLamination(models.Model):
    name = models.CharField(max_length=255, verbose_name="Тип ламинации", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тип ламинации'
        verbose_name_plural = 'Типы ламинации'


class TypeLamination2(models.Model):
    name = models.CharField(max_length=255, verbose_name="Вид ламинации", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Вид ламинации'
        verbose_name_plural = 'Виды ламинации'


class SealInternal(models.Model):
    name = models.CharField(max_length=255, verbose_name="Исполнение внутри", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Исполнение внутри'
        verbose_name_plural = 'Исполнение внутри'


class SealOutside(models.Model):
    name = models.CharField(max_length=255, verbose_name="Исполнение снаружи", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Исполнение снаружи'
        verbose_name_plural = 'Исполнение снаружи'


class SealBasic(models.Model):
    name = models.CharField(max_length=255, verbose_name="Исполнение основы детали", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Исполнение основы детали'
        verbose_name_plural = 'Исполнение основы детали'


class Lamination(models.Model):
    type_lamination = models.ForeignKey(TypeLamination, on_delete=models.SET_NULL, verbose_name="Тип ламинации",
                                        blank=True, null=True)
    type_lamination1 = models.ForeignKey(TypeLamination2, on_delete=models.SET_NULL, verbose_name="Вид ламинации",
                                         blank=True, null=True)
    seal_internal = models.ForeignKey(SealInternal, on_delete=models.SET_NULL, verbose_name="Исполнение внутри",
                                      blank=True, null=True)
    seal_outside = models.ForeignKey(SealOutside, on_delete=models.SET_NULL, verbose_name="Исполнение снаружи",
                                     blank=True, null=True)
    seal_basic = models.ForeignKey(SealBasic, on_delete=models.SET_NULL, verbose_name="Исполнение основы детали",
                                   blank=True, null=True)

    def __str__(self):
        return f'№ {self.pk} {self.type_lamination.name}'

    class Meta:
        verbose_name = 'Ламинация'
        verbose_name_plural = 'Ламинации'


# class Sealant(models.Model):
#     color = models.CharField(max_length=255, verbose_name="Цвет", blank=True, null=True)
#     execution_outside = models.CharField(max_length=255, verbose_name="Исполнение снаружи", blank=True, null=True)
#     execution_inside = models.CharField(max_length=255, verbose_name="Исполнение внутри", blank=True, null=True)
#     shtapik = models.CharField(max_length=255, verbose_name="Штапик", blank=True, null=True)
#
#     def __str__(self):
#         return self.color
#
#     class Meta:
#         verbose_name = 'Уплотнитель'
#         verbose_name_plural = 'Уплотнители'


class Shtapik(models.Model):
    name = models.CharField(max_length=255, verbose_name="Штапик", blank=True, null=True)

    def __str__(self):
        return f'№ {self.pk} имя : {self.name}'

    class Meta:
        verbose_name = 'Штапик'
        verbose_name_plural = 'Штапики'


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


# class SealOutside(models.Model):
#     name = models.CharField(max_length=255, verbose_name="Уплотнение снаружи", blank=True, null=True)
#
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         verbose_name = 'Уплотнение снаружи'
#         verbose_name_plural = 'Уплотнение снаружи'


class SealRebate(models.Model):
    name = models.CharField(max_length=255, verbose_name="Уплотнение притвора", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Уплотнение притвора'
        verbose_name_plural = 'Уплотнение притвора'


# class SealInternal(models.Model):
#     name = models.CharField(max_length=255, verbose_name="Уплотнение внутренее", blank=True, null=True)
#
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         verbose_name = 'Уплотнение внутренее'
#         verbose_name_plural = 'Уплотнение внутренее'





class Shpros(models.Model):
    name = models.CharField(max_length=255, verbose_name="Шпрос", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Шпрос'
        verbose_name_plural = 'Шпросы'


# class Shtapik(models.Model):
#     name = models.CharField(max_length=255, verbose_name="Штапик", blank=True, null=True)
#
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         verbose_name = 'Штапик'
#         verbose_name_plural = 'Штапики'


class Sash(models.Model):
    name = models.CharField(max_length=255, verbose_name="Створка", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Створка'
        verbose_name_plural = 'Створки'


class Gorbylki(models.Model):
    name = models.CharField(max_length=255, verbose_name="Горбыльки", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Горбыльки'
        verbose_name_plural = 'Горбыльки'


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


class OtherComplectation(models.Model):
    name = models.CharField(max_length=255, verbose_name="Прочее комплектующие", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Прочее комплектующие'
        verbose_name_plural = 'Прочее комплектующие'


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
        return f' Работы № {self.pk} {self.name} на сумму {self.price} BYN'

    class Meta:
        verbose_name = 'Просчет работы'
        verbose_name_plural = 'Просчеты работ'
