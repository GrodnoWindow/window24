# Generated by Django 4.1.2 on 2023-08-12 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0010_remove_passportdetails_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='number',
            field=models.IntegerField(blank=True, max_length=255, null=True, verbose_name='Номер договора'),
        ),
    ]
