# Generated by Django 4.1.2 on 2023-03-05 20:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('measurer_window', '0008_remove_windowsillcalc_price_output_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='windowsill',
            old_name='price',
            new_name='price_in_byn',
        ),
        migrations.RenameField(
            model_name='windowsillcalc',
            old_name='price_byn',
            new_name='price_in_byn',
        ),
        migrations.RenameField(
            model_name='windowsillcalc',
            old_name='price_currency',
            new_name='price_in_currency',
        ),
    ]