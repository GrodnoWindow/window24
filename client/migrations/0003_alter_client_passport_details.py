# Generated by Django 4.1.2 on 2023-07-23 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0002_passportdetails_contract_client_contract_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='passport_details',
            field=models.ManyToManyField(blank=True, to='client.passportdetails'),
        ),
    ]