# Generated by Django 4.1.2 on 2023-02-20 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculation', '0007_windowsillcalc_color'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='casingcalc',
            name='installation',
        ),
        migrations.RemoveField(
            model_name='flashingcalc',
            name='installation',
        ),
        migrations.RemoveField(
            model_name='internalslopecalc',
            name='installation',
        ),
        migrations.RemoveField(
            model_name='lowtidescalc',
            name='installation',
        ),
        migrations.RemoveField(
            model_name='slopesofmetalcalc',
            name='installation',
        ),
        migrations.RemoveField(
            model_name='visorscalc',
            name='installation',
        ),
        migrations.RemoveField(
            model_name='windowsillcalc',
            name='color',
        ),
        migrations.RemoveField(
            model_name='windowsillcalc',
            name='installation',
        ),
        migrations.AddField(
            model_name='casingcalc',
            name='color_id',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Цвет'),
        ),
        migrations.AddField(
            model_name='casingcalc',
            name='installation_id',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Установка'),
        ),
        migrations.AddField(
            model_name='flashingcalc',
            name='color_id',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Цвет'),
        ),
        migrations.AddField(
            model_name='flashingcalc',
            name='installation_id',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Установка'),
        ),
        migrations.AddField(
            model_name='internalslopecalc',
            name='color_id',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Цвет'),
        ),
        migrations.AddField(
            model_name='internalslopecalc',
            name='installation_id',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Установка'),
        ),
        migrations.AddField(
            model_name='lowtidescalc',
            name='color_id',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Цвет'),
        ),
        migrations.AddField(
            model_name='lowtidescalc',
            name='installation_id',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Установка'),
        ),
        migrations.AddField(
            model_name='slopesofmetalcalc',
            name='color_id',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Цвет'),
        ),
        migrations.AddField(
            model_name='slopesofmetalcalc',
            name='installation_id',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Установка'),
        ),
        migrations.AddField(
            model_name='visorscalc',
            name='color_id',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Цвет'),
        ),
        migrations.AddField(
            model_name='visorscalc',
            name='installation_id',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Установка'),
        ),
        migrations.AddField(
            model_name='windowsillcalc',
            name='color_id',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Цвет'),
        ),
        migrations.AddField(
            model_name='windowsillcalc',
            name='installation_id',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Установка'),
        ),
    ]