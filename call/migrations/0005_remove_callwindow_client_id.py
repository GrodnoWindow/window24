# Generated by Django 4.1.2 on 2023-02-21 14:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('call', '0004_alter_callwindow_call_status_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='callwindow',
            name='client_id',
        ),
    ]
