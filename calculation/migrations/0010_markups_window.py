# Generated by Django 4.1.2 on 2022-10-15 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculation', '0009_rename_low_tides_lowtidescalc_low_tides_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='markups',
            name='window',
            field=models.FloatField(default=0.0, max_length=255, verbose_name='Окна в %'),
        ),
    ]
