# Generated by Django 4.1.2 on 2023-01-16 12:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('measurer', '0002_alter_measurement_executor_alter_measurement_manager_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='measurement',
            name='number',
            field=models.CharField(default=django.utils.timezone.now, max_length=255, verbose_name='Номер клиента'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='measurement',
            name='client',
            field=models.CharField(max_length=255, verbose_name='Имя клиента'),
        ),
    ]
