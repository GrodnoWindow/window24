# Generated by Django 3.2 on 2022-10-13 19:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calculation', '0004_windowsillcalc'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='windowsillcalc',
            name='sum',
        ),
    ]
