# Generated by Django 4.1.2 on 2023-01-16 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('measurer', '0004_alter_measurement_address_alter_measurement_client_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='measurement',
            name='who_updated',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Кем обновлено'),
        ),
    ]
