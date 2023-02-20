# Generated by Django 4.1.2 on 2023-02-20 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculation', '0009_alter_visorscalc_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='casingcalc',
            old_name='fastening',
            new_name='fastening_id',
        ),
        migrations.AddField(
            model_name='slopesofmetalcalc',
            name='fastening_id',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Крепление'),
        ),
        migrations.AlterField(
            model_name='slopesofmetalcalc',
            name='markups_type',
            field=models.CharField(max_length=255, verbose_name='Наценка'),
        ),
    ]
