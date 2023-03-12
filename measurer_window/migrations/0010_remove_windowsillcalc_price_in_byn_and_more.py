# Generated by Django 4.1.2 on 2023-03-10 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('measurer_window', '0009_windowsillconnection_windowsillplug_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='windowsillcalc',
            name='price_in_byn',
        ),
        migrations.RemoveField(
            model_name='windowsillcalc',
            name='price_in_currency',
        ),
        migrations.AddField(
            model_name='windowsillcalc',
            name='sum_connection_byn',
            field=models.FloatField(blank=True, default=0.0, max_length=255, null=True, verbose_name='Цена соединитеей в BYN'),
        ),
        migrations.AddField(
            model_name='windowsillcalc',
            name='sum_connection_currency',
            field=models.FloatField(blank=True, default=0.0, max_length=255, null=True, verbose_name='Цена соединителей в EUR/USD'),
        ),
        migrations.AddField(
            model_name='windowsillcalc',
            name='sum_in_byn',
            field=models.FloatField(blank=True, default=0.0, max_length=255, null=True, verbose_name='Цена BYN'),
        ),
        migrations.AddField(
            model_name='windowsillcalc',
            name='sum_in_currency',
            field=models.FloatField(blank=True, default=0.0, max_length=255, null=True, verbose_name='Цена EUR/USD'),
        ),
        migrations.AddField(
            model_name='windowsillcalc',
            name='sum_plug_byn',
            field=models.FloatField(blank=True, default=0.0, max_length=255, null=True, verbose_name='Цена заглушек в BYN'),
        ),
        migrations.AddField(
            model_name='windowsillcalc',
            name='sum_plug_currency',
            field=models.FloatField(blank=True, default=0.0, max_length=255, null=True, verbose_name='Цена заглушек в EUR/USD'),
        ),
        migrations.AddField(
            model_name='windowsillcalc',
            name='sum_windowsill_byn',
            field=models.FloatField(blank=True, default=0.0, max_length=255, null=True, verbose_name='Цена подоконника в BYN'),
        ),
        migrations.AddField(
            model_name='windowsillcalc',
            name='sum_windowsill_currency',
            field=models.FloatField(blank=True, default=0.0, max_length=255, null=True, verbose_name='Цена подоконника в EUR/USD'),
        ),
        migrations.AlterField(
            model_name='windowsillcalc',
            name='linear_meter',
            field=models.FloatField(blank=True, default=0.0, max_length=255, null=True, verbose_name='В метрах погонных'),
        ),
        migrations.AlterField(
            model_name='windowsillcalc',
            name='square_meter',
            field=models.FloatField(blank=True, default=0.0, max_length=255, null=True, verbose_name='В метрах квадратных'),
        ),
    ]