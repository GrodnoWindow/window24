# Generated by Django 4.1.2 on 2023-01-17 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('measurer', '0008_rename_final_amounts_measurement_final_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='measurement',
            name='logs',
            field=models.TextField(blank=True, null=True),
        ),
    ]
