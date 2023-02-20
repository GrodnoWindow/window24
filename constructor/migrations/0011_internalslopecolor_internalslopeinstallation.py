# Generated by Django 4.1.2 on 2023-02-20 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('constructor', '0010_flashingcolor_flashinginstallation'),
    ]

    operations = [
        migrations.CreateModel(
            name='InternalSlopeColor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Название цвета')),
            ],
            options={
                'verbose_name': 'Цвет внутренних откосов',
                'verbose_name_plural': 'Цвета внутренних откосов',
            },
        ),
        migrations.CreateModel(
            name='InternalSlopeInstallation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Название монтажа')),
                ('price', models.FloatField(blank=True, default=0.0, null=True, verbose_name='Цена монтажа')),
            ],
            options={
                'verbose_name': 'Монтаж внутренних откосов',
                'verbose_name_plural': 'Монтажи внутренних откосов',
            },
        ),
    ]