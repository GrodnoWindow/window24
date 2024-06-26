# Generated by Django 4.1.2 on 2023-09-14 17:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('constructor', '0028_slopesofmetalcolor_slopes_of_metal_provider'),
    ]

    operations = [
        migrations.CreateModel(
            name='SlopesOfMetalLowTides',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Название замка')),
                ('price_input', models.FloatField(blank=True, default=0.0, null=True, verbose_name='Цена замка')),
                ('slopes_of_metal_provider', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='constructor.slopesofmetalprovider', verbose_name='Поставщик')),
            ],
            options={
                'verbose_name': 'Замок откосов из металла',
                'verbose_name_plural': 'Замки откосов из металла',
            },
        ),
        migrations.AddField(
            model_name='slopesofmetal',
            name='slopes_of_metal_low_tides',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='constructor.slopesofmetallowtides', verbose_name='Отлив'),
        ),
    ]
