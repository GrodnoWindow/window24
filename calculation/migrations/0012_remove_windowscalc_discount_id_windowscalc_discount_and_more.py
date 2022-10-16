# Generated by Django 4.1.2 on 2022-10-15 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculation', '0011_rename_discount_windowdiscount_value_windowscalc'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='windowscalc',
            name='discount_id',
        ),
        migrations.AddField(
            model_name='windowscalc',
            name='discount',
            field=models.FloatField(blank=True, max_length=255, null=True, verbose_name='Скидка на окно'),
        ),
        migrations.AlterField(
            model_name='windowscalc',
            name='currency',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Валюта'),
        ),
    ]
