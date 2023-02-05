# Generated by Django 4.1.2 on 2023-02-02 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miscalculation', '0001_initial'),
        ('client', '0002_remove_prompter_built_from'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='miscalculation',
            field=models.ManyToManyField(blank=True, to='miscalculation.miscalculation', verbose_name='Просчеты'),
        ),
        migrations.AddField(
            model_name='client',
            name='numbers',
            field=models.ManyToManyField(blank=True, to='client.number'),
        ),
        migrations.AddField(
            model_name='client',
            name='prompter',
            field=models.ManyToManyField(blank=True, to='client.prompter'),
        ),
        migrations.AddField(
            model_name='prompter',
            name='address',
            field=models.CharField(blank=True, default=False, max_length=255, verbose_name=''),
        ),
        migrations.AddField(
            model_name='prompter',
            name='built_from_other',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Из чего построен'),
        ),
        migrations.AddField(
            model_name='prompter',
            name='floor',
            field=models.CharField(blank=True, default=False, max_length=255, verbose_name='Комнаты'),
        ),
        migrations.AddField(
            model_name='prompter',
            name='layout',
            field=models.CharField(blank=True, default=False, max_length=255, verbose_name=''),
        ),
        migrations.AddField(
            model_name='prompter',
            name='reason_window_change',
            field=models.CharField(blank=True, default=False, max_length=255, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='prompter',
            name='installation_room',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Комната установки'),
        ),
        migrations.AlterField(
            model_name='prompter',
            name='mounting_all',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Монтаж отливов/подоконников'),
        ),
        migrations.AlterField(
            model_name='prompter',
            name='type_home',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Тип дома'),
        ),
        migrations.AlterField(
            model_name='prompter',
            name='winter_cold',
            field=models.CharField(blank=True, default=False, max_length=255, verbose_name='Зимой холодно'),
        ),
    ]