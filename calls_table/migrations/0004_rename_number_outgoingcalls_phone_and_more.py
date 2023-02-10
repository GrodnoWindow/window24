# Generated by Django 4.1.2 on 2023-02-10 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calls_table', '0003_outgoingcalls'),
    ]

    operations = [
        migrations.RenameField(
            model_name='outgoingcalls',
            old_name='number',
            new_name='phone',
        ),
        migrations.AddField(
            model_name='outgoingcalls',
            name='number_phone',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
