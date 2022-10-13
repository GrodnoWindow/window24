# Generated by Django 4.1.2 on 2022-10-13 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('constructor', '0002_delete_windowsilldankekomfort_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='constructor',
            old_name='price',
            new_name='price_input',
        ),
        migrations.AddField(
            model_name='constructor',
            name='price_output',
            field=models.FloatField(blank=True, default=0.0, max_length=255, null=True),
        ),
    ]
