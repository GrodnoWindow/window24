# Generated by Django 4.1.2 on 2023-03-05 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('measurer_window', '0004_order_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='windowsill_calc',
            field=models.ManyToManyField(blank=True, null=True, to='measurer_window.windowsillcalc'),
        ),
    ]
