# Generated by Django 4.1.2 on 2023-09-15 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculation', '0010_slopesofmetalcalc_lock_width_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='slopesofmetalcalc',
            name='lock_length',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Замок длинна ( общая )'),
        ),
        migrations.AddField(
            model_name='slopesofmetalcalc',
            name='low_tides_length',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Отлив длинна ( общая ) '),
        ),
    ]
