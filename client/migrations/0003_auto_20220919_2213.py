# Generated by Django 3.2 on 2022-09-19 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('call', '0005_alter_call_datetime'),
        ('client', '0002_client_calls'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='calls',
        ),
        migrations.AddField(
            model_name='client',
            name='calls',
            field=models.ManyToManyField(to='call.Call'),
        ),
    ]