# Generated by Django 3.2 on 2022-10-11 21:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calculation', '0002_exchangerates'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='exchangerates',
            options={'verbose_name': 'Курс валют', 'verbose_name_plural': 'Курсы валют'},
        ),
    ]
