# Generated by Django 4.1.2 on 2023-02-20 16:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calculation', '0005_rename_casing_markups_casingmarkups_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='internalslopecalc',
            options={'verbose_name': 'Просчет внутреннего откоса ', 'verbose_name_plural': 'Просчеты внутренних откосов'},
        ),
        migrations.AlterModelOptions(
            name='mountingmaterialscalc',
            options={'verbose_name': 'Просчет монтажных материалов', 'verbose_name_plural': 'Просчеты монтажных материалов'},
        ),
    ]