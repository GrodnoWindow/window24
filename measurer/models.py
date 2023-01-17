from django.db import models
from users.models import User
from client.models import Client
from users.models import User


class Agreements(models.Model):
    image = models.ImageField(upload_to='Agreements/', blank=True, null=True)

    def __str__(self):
        return str(self.image)

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'


class Measurement(models.Model):
    client = models.CharField(max_length=255, blank=True, verbose_name='Имя клиента')
    address = models.CharField(max_length=255, blank=True, verbose_name='Адрес замера')
    number = models.CharField(max_length=255,blank=True, verbose_name='Номер клиента')
    time = models.TimeField(blank=True, verbose_name='Время замера')
    comment = models.CharField(max_length=255,blank=True, verbose_name='Комментарий к замеру')
    date = models.DateField(auto_created=True, blank=True,verbose_name='Дата замера')
    manager = models.CharField(max_length=255, null=True, verbose_name='Менеджер', blank=True)
    executor = models.ForeignKey(User, null=True,on_delete=models.CASCADE, verbose_name='Исполнитель', blank=True)
    status = models.CharField(max_length=255, blank=True, verbose_name='Статус')
    time_create = models.DateTimeField(auto_now_add=True, blank=True, verbose_name='Время создания')
    time_updated = models.DateTimeField(verbose_name='Время обновления', blank=True,)
    who_updated = models.CharField(max_length=255, null=True, verbose_name='Кем обновлено', blank=True)
    is_active = models.BooleanField(default=True, verbose_name='Активна')
    agreements = models.CharField(max_length=255, verbose_name='Изображения', blank=True, null=True)
    preliminary_amount = models.CharField(max_length=255, verbose_name='Предварительная сумма', blank=True, null=True)
    final_amount = models.CharField(max_length=255, verbose_name='Окончательная сумма', blank=True, null=True)
    logs = models.TextField(blank=True, null=True, verbose_name='Логи замера')

    def __str__(self):
        return f'{self.client} {self.address}'

    class Meta:
        verbose_name = 'Замер'
        verbose_name_plural = 'Замеры'