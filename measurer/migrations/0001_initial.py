# Generated by Django 4.1.2 on 2023-01-16 09:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('client', '0002_client_miscalculation_client_numbers_client_prompter'),
    ]

    operations = [
        migrations.CreateModel(
            name='Measurement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_created=True, verbose_name='Дата замера')),
                ('address', models.CharField(max_length=255, verbose_name='Адрес замера')),
                ('time', models.CharField(max_length=255, verbose_name='Время замера')),
                ('comment', models.CharField(max_length=255, verbose_name='Комментарий к замеру')),
                ('status', models.CharField(max_length=255, verbose_name='Статус')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('time_updated', models.DateTimeField(verbose_name='Время обновления')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активна')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.client', verbose_name='Клиент')),
                ('executor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='executor', to=settings.AUTH_USER_MODEL, verbose_name='Замерщик')),
                ('manager', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='manager', to=settings.AUTH_USER_MODEL, verbose_name='Менеджер')),
                ('who_updated', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='who_update', to=settings.AUTH_USER_MODEL, verbose_name='Кем обновлено')),
            ],
            options={
                'verbose_name': 'Замер',
                'verbose_name_plural': 'Замеры',
            },
        ),
    ]
