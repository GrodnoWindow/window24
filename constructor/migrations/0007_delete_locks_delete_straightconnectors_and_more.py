# Generated by Django 4.1.2 on 2023-05-06 12:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('constructor', '0006_rename_provider_casing_casing_casing_provider_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Locks',
        ),
        migrations.DeleteModel(
            name='StraightConnectors',
        ),
        migrations.DeleteModel(
            name='SupplyValve',
        ),
        migrations.AlterModelOptions(
            name='producttypedoor',
            options={'verbose_name': 'Тип изделия двери', 'verbose_name_plural': 'Тип изделия двери'},
        ),
        migrations.AlterModelOptions(
            name='works',
            options={'verbose_name': 'Работы', 'verbose_name_plural': 'Работы'},
        ),
    ]