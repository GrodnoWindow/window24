# Generated by Django 4.1.2 on 2022-11-24 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculation', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='constructor',
            name='lowtides_calc',
            field=models.ManyToManyField(blank=True, to='calculation.lowtidescalc', verbose_name='Просчеты отливов'),
        ),
    ]
