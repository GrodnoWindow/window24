# Generated by Django 3.2 on 2022-09-27 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('call', '0006_remove_call_id_client'),
        ('client', '0005_auto_20220927_0428'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='calls',
            field=models.ManyToManyField(null=True, to='call.Call'),
        ),
        migrations.AlterField(
            model_name='client',
            name='number',
            field=models.ManyToManyField(null=True, to='client.Number'),
        ),
    ]
