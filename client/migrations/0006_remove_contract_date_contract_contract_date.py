# Generated by Django 4.1.2 on 2023-07-23 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0005_remove_contract_date_contract_date_contract'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contract',
            name='date_contract',
        ),
        migrations.AddField(
            model_name='contract',
            name='date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]