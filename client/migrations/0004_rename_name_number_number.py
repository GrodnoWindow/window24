# Generated by Django 3.2 on 2022-10-07 18:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0003_auto_20221007_1953'),
    ]

    operations = [
        migrations.RenameField(
            model_name='number',
            old_name='name',
            new_name='number',
        ),
    ]