from django.db import models

from call.models import Call
from miscalculation.models import Miscalculation
from complaint.models import Complaint


class Prompter(models.Model):
    category_select = models.IntegerField(blank=True, null=True, verbose_name="Категория выбора")
    main_statements = models.CharField(max_length=255, blank=True, verbose_name="Основные высказывания")
    type_home = models.IntegerField(blank=True, null=True, verbose_name="Тип дома")
    built_from = models.IntegerField(blank=True, null=True, verbose_name="Из чего построен")
    sun_heating = models.BooleanField(default=False, blank=True, verbose_name='Летом солнце нагревает')
    weak_light = models.BooleanField(default=False, blank=True,  verbose_name='Мало света ')
    noise_outside = models.BooleanField(default=False, blank=True,  verbose_name='Шум за окном')
    winter_cold = models.BooleanField(default=False, blank=True,  verbose_name='Зимой холодно')
    rose_of_wind = models.BooleanField(default=False, blank=True,  verbose_name='Роза ветров')
    children = models.BooleanField(default=False, blank=True,  verbose_name='Есть ли дети')
    installation_room = models.IntegerField(blank=True, null=True, verbose_name="Комната установки")
    special_offers = models.CharField(max_length=255, blank=True,  verbose_name='Специальные предложения')
    solution_window = models.CharField(max_length=255, blank=True,  verbose_name='Почему решили поменять окно')
    only_window = models.BooleanField(default=False, blank=True,  verbose_name='Только окно')
    mounting_all = models.IntegerField(blank=True, null=True, verbose_name="Монтаж отливов/подоконников")
    slopes = models.BooleanField(default=False, blank=True,  verbose_name='Отделка откосов')
    mosquito_net = models.BooleanField(default=False, blank=True,  verbose_name='Москитная сетка')
    room = models.CharField(max_length=255, blank=True,  verbose_name='В какую комнату установка')
    individual_wishes = models.CharField(max_length=255, blank=True,  verbose_name='Индивидуальные пожелания')


    def __str__(self):
        return self.main_statements


class Number(models.Model):
    number = models.CharField(max_length=255, blank=True)
    name = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.number


class Address(models.Model):
    name = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name


class Client(models.Model):
    author = models.CharField(max_length=255, blank=True)
    name = models.CharField(max_length=255, blank=True)
    numbers = models.ManyToManyField(Number, blank=True)
    addresses = models.ManyToManyField(Address, blank=True)
    prompter = models.ManyToManyField(Prompter, blank=True)
    time_created = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    calls = models.ManyToManyField(Call, blank=True)
    miscalculation = models.ManyToManyField(Miscalculation, verbose_name="Просчеты", blank=True)
    complaints = models.ManyToManyField(Complaint, verbose_name="Жалобы", blank=True)

    def __str__(self):
        return self.name
