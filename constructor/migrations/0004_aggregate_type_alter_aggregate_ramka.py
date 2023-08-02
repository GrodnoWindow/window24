# Generated by Django 4.1.2 on 2023-08-02 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('constructor', '0003_aggregate_article_aggregate_camera_aggregate_ramka'),
    ]

    operations = [
        migrations.AddField(
            model_name='aggregate',
            name='type',
            field=models.IntegerField(choices=[(1, 'Sendvich'), (2, 'Энергосберегающие'), (3, 'EnergyAir'), (4, 'Тонированные'), (5, 'феникс клер'), (6, 'феникс бронза'), (7, 'феникс грей'), (8, 'CRYSTALVISION'), (9, 'Антирезонансные'), (10, 'Антивандальные'), (11, 'триплекс')], default=1, verbose_name='Тип'),
        ),
        migrations.AlterField(
            model_name='aggregate',
            name='ramka',
            field=models.IntegerField(choices=[(1, 'Стандарт'), (2, 'Черная'), (3, 'Белая')], default=1, verbose_name='Рамка'),
        ),
    ]
