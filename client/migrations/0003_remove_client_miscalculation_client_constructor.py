# Generated by Django 4.2 on 2023-05-08 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculation', '0002_rename_sploes_of_metal_calc_constructor_slopes_of_metal_calc'),
        ('client', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='miscalculation',
        ),
        migrations.AddField(
            model_name='client',
            name='constructor',
            field=models.ManyToManyField(blank=True, to='calculation.constructor', verbose_name='Просчеты конструкторов'),
        ),
    ]