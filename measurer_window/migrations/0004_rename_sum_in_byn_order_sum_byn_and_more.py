# Generated by Django 4.1.2 on 2023-03-07 18:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('measurer_window', '0003_rename_sum_in_materials_in_byn_order_sum_materials_in_byn_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='sum_in_byn',
            new_name='sum_byn',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='sum_in_currency',
            new_name='sum_currency',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='sum_materials_in_byn',
            new_name='sum_materials_byn',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='sum_materials_in_currency',
            new_name='sum_materials_currency',
        ),
    ]