# Generated by Django 4.1.2 on 2023-02-20 17:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('constructor', '0006_windowsillcolor_alter_windowsill_color'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='casing',
            name='color',
        ),
        migrations.RemoveField(
            model_name='flashing',
            name='color',
        ),
        migrations.RemoveField(
            model_name='internalslope',
            name='color',
        ),
        migrations.RemoveField(
            model_name='lowtides',
            name='color',
        ),
        migrations.RemoveField(
            model_name='slopesofmetal',
            name='color',
        ),
        migrations.RemoveField(
            model_name='visors',
            name='color',
        ),
        migrations.RemoveField(
            model_name='windowsill',
            name='color',
        ),
        migrations.DeleteModel(
            name='WindowsillColor',
        ),
    ]