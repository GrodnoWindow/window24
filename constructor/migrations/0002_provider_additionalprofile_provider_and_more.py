# Generated by Django 4.2 on 2023-04-25 13:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('constructor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Поставщик')),
                ('currency', models.CharField(blank=True, max_length=255, null=True, verbose_name='Валюта')),
            ],
            options={
                'verbose_name': 'Поставщик',
                'verbose_name_plural': 'Поставщики',
            },
        ),
        migrations.AddField(
            model_name='additionalprofile',
            name='provider',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='constructor.provider', verbose_name='Поставщик'),
        ),
        migrations.AddField(
            model_name='connectionprofile',
            name='provider',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='constructor.provider', verbose_name='Поставщик'),
        ),
        migrations.AddField(
            model_name='othercomplectation',
            name='provider',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='constructor.provider', verbose_name='Поставщик'),
        ),
        migrations.AlterField(
            model_name='casing',
            name='provider',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='constructor.provider', verbose_name='Поставщик'),
        ),
        migrations.AlterField(
            model_name='flashing',
            name='provider',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='constructor.provider', verbose_name='Поставщик'),
        ),
        migrations.AlterField(
            model_name='internalslope',
            name='provider',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='constructor.provider', verbose_name='Поставщик'),
        ),
        migrations.AlterField(
            model_name='lowtides',
            name='provider',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='constructor.provider', verbose_name='Поставщик'),
        ),
        migrations.AlterField(
            model_name='mountingmaterialstype',
            name='provider',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='constructor.provider', verbose_name='Поставщик'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='provider',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='constructor.provider', verbose_name='Поставщик'),
        ),
        migrations.AlterField(
            model_name='slopesofmetal',
            name='provider',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='constructor.provider', verbose_name='Поставщик'),
        ),
        migrations.AlterField(
            model_name='visors',
            name='provider',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='constructor.provider', verbose_name='Поставщик'),
        ),
        migrations.AlterField(
            model_name='windowsill',
            name='provider',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='constructor.provider', verbose_name='Поставщик'),
        ),
    ]
