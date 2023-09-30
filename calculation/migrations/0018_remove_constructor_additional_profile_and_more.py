# Generated by Django 4.1.2 on 2023-09-30 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculation', '0017_remove_connectionprofilecalc_width_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='constructor',
            name='additional_profile',
        ),
        migrations.RemoveField(
            model_name='constructor',
            name='connection_profile',
        ),
        migrations.RemoveField(
            model_name='constructor',
            name='other_complectation',
        ),
        migrations.AddField(
            model_name='constructor',
            name='additional_profile_calc',
            field=models.ManyToManyField(blank=True, null=True, to='calculation.additionalprofilecalc', verbose_name='Доборные профиля'),
        ),
        migrations.AddField(
            model_name='constructor',
            name='connection_profile_calc',
            field=models.ManyToManyField(blank=True, null=True, to='calculation.connectionprofilecalc', verbose_name='Соединительные профиля'),
        ),
        migrations.AddField(
            model_name='constructor',
            name='other_complectation_profile_calc',
            field=models.ManyToManyField(blank=True, null=True, to='calculation.othercomplectationprofilecalc', verbose_name='Прочее комплектующие'),
        ),
    ]
