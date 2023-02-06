# Generated by Django 4.1.2 on 2023-02-06 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agreements',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='Agreements/')),
            ],
            options={
                'verbose_name': 'Изображение',
                'verbose_name_plural': 'Изображения',
            },
        ),
        migrations.CreateModel(
            name='Measurement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_created=True, blank=True, verbose_name='Дата замера')),
                ('client', models.CharField(blank=True, max_length=255, verbose_name='Имя клиента')),
                ('address', models.CharField(blank=True, max_length=255, verbose_name='Адрес замера')),
                ('number', models.CharField(blank=True, max_length=255, verbose_name='Номер клиента')),
                ('time', models.TimeField(blank=True, verbose_name='Время замера')),
                ('comment', models.CharField(blank=True, max_length=255, verbose_name='Комментарий к замеру')),
                ('manager', models.CharField(blank=True, max_length=255, null=True, verbose_name='Менеджер')),
                ('status', models.CharField(blank=True, max_length=255, verbose_name='Статус')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('time_updated', models.DateTimeField(blank=True, verbose_name='Время обновления')),
                ('who_updated', models.CharField(blank=True, max_length=255, null=True, verbose_name='Кем обновлено')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активна')),
                ('agreements', models.CharField(blank=True, max_length=255, null=True, verbose_name='Изображения')),
                ('preliminary_amount', models.CharField(blank=True, max_length=255, null=True, verbose_name='Предварительная сумма')),
                ('final_amount', models.CharField(blank=True, max_length=255, null=True, verbose_name='Окончательная сумма')),
                ('logs', models.TextField(blank=True, null=True, verbose_name='Логи замера')),
            ],
            options={
                'verbose_name': 'Замер',
                'verbose_name_plural': 'Замеры',
            },
        ),
    ]
