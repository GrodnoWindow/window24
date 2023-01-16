from django.db import models
from users.models import User
from client.models import Client
from users.models import User


class Measurement(models.Model):
    client = models.CharField(max_length=255, blank=True, verbose_name='Имя клиента')
    address = models.CharField(max_length=255, blank=True, verbose_name='Адрес замера')
    number = models.CharField(max_length=255,blank=True, verbose_name='Номер клиента')
    time = models.CharField(max_length=255,blank=True, verbose_name='Время замера')
    comment = models.CharField(max_length=255,blank=True, verbose_name='Комментарий к замеру')
    date = models.DateField(auto_created=True, blank=True,verbose_name='Дата замера')
    manager = models.ForeignKey(User, on_delete=models.CASCADE, null=True, verbose_name='Менеджер',
                                related_name='manager', blank=True)
    executor = models.ForeignKey(User, on_delete=models.CASCADE, null=True, verbose_name='Замерщик',
                                 related_name='executor', blank=True)
    status = models.CharField(max_length=255, blank=True, verbose_name='Статус')
    time_create = models.DateTimeField(auto_now_add=True, blank=True, verbose_name='Время создания')
    time_updated = models.DateTimeField(verbose_name='Время обновления', blank=True,)
    who_updated = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='who_update',
                                    verbose_name='Кем обновлено', blank=True)
    is_active = models.BooleanField(default=True, verbose_name='Активна')

    def __str__(self):
        return f'{self.client} {self.address}'

    class Meta:
        verbose_name = 'Замер'
        verbose_name_plural = 'Замеры'