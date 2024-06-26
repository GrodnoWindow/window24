# Generated by Django 4.1.2 on 2023-08-23 17:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('constructor', '0020_internalslopef_internalslopelatch_internalslopelid_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='InternalSlopeCasing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Название')),
                ('price_input', models.FloatField(blank=True, null=True, verbose_name='Цена')),
            ],
            options={
                'verbose_name': 'Наличник внутренние откосы',
                'verbose_name_plural': 'Наличник внутренних откосов',
            },
        ),
        migrations.CreateModel(
            name='InternalSlopeStartProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Название')),
                ('price_input', models.FloatField(blank=True, null=True, verbose_name='Цена')),
            ],
            options={
                'verbose_name': 'Старт профиль внутренние откосы',
                'verbose_name_plural': 'Старт профиля внутренних откосов',
            },
        ),
        migrations.AddField(
            model_name='internalslope',
            name='internal_slope_casing',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='constructor.internalslopecasing', verbose_name='наличник'),
        ),
        migrations.AddField(
            model_name='internalslope',
            name='internal_slope_start_profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='constructor.internalslopestartprofile', verbose_name='Стартовый профиль'),
        ),
    ]
