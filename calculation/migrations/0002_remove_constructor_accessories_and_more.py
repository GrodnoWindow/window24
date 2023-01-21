# Generated by Django 4.1.2 on 2023-01-19 19:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('constructor', '0002_door_lamination_sealant'),
        ('calculation', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='constructor',
            name='accessories',
        ),
        migrations.RemoveField(
            model_name='constructor',
            name='bay_window_to_profile60',
        ),
        migrations.RemoveField(
            model_name='constructor',
            name='bay_window_to_profile70',
        ),
        migrations.RemoveField(
            model_name='constructor',
            name='connector_90g',
        ),
        migrations.RemoveField(
            model_name='constructor',
            name='extensions_to_profile60',
        ),
        migrations.RemoveField(
            model_name='constructor',
            name='extensions_to_profile70',
        ),
        migrations.RemoveField(
            model_name='constructor',
            name='favorite_positions',
        ),
        migrations.RemoveField(
            model_name='constructor',
            name='flashing',
        ),
        migrations.RemoveField(
            model_name='constructor',
            name='flashing_metal',
        ),
        migrations.RemoveField(
            model_name='constructor',
            name='free_positions',
        ),
        migrations.RemoveField(
            model_name='constructor',
            name='lamination_inside',
        ),
        migrations.RemoveField(
            model_name='constructor',
            name='lamination_outside',
        ),
        migrations.RemoveField(
            model_name='constructor',
            name='locks',
        ),
        migrations.RemoveField(
            model_name='constructor',
            name='note',
        ),
        migrations.RemoveField(
            model_name='constructor',
            name='platband',
        ),
        migrations.RemoveField(
            model_name='constructor',
            name='price_input',
        ),
        migrations.RemoveField(
            model_name='constructor',
            name='price_material',
        ),
        migrations.RemoveField(
            model_name='constructor',
            name='price_window',
        ),
        migrations.RemoveField(
            model_name='constructor',
            name='products_install',
        ),
        migrations.RemoveField(
            model_name='constructor',
            name='profile_weight',
        ),
        migrations.RemoveField(
            model_name='constructor',
            name='pvc_slopes',
        ),
        migrations.RemoveField(
            model_name='constructor',
            name='seal_color',
        ),
        migrations.RemoveField(
            model_name='constructor',
            name='seal_internal',
        ),
        migrations.RemoveField(
            model_name='constructor',
            name='seal_outside',
        ),
        migrations.RemoveField(
            model_name='constructor',
            name='seal_rebate',
        ),
        migrations.RemoveField(
            model_name='constructor',
            name='shpros',
        ),
        migrations.RemoveField(
            model_name='constructor',
            name='straight_connectors',
        ),
        migrations.RemoveField(
            model_name='constructor',
            name='supply_valve',
        ),
        migrations.RemoveField(
            model_name='constructor',
            name='visors',
        ),
        migrations.AddField(
            model_name='constructor',
            name='door',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='constructor.door', verbose_name='Двери'),
        ),
        migrations.AddField(
            model_name='constructor',
            name='gorbylki',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Горбыльки'),
        ),
        migrations.AddField(
            model_name='constructor',
            name='lamination',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='constructor.lamination', verbose_name='Ламинация'),
        ),
        migrations.AddField(
            model_name='constructor',
            name='sealant',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='constructor.sealant', verbose_name='Уплотнитель'),
        ),
        migrations.AlterField(
            model_name='constructor',
            name='aggregate',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='constructor.aggregate', verbose_name='Заполнитель'),
        ),
        migrations.AlterField(
            model_name='constructor',
            name='handles',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='ручки'),
        ),
        migrations.AlterField(
            model_name='constructor',
            name='sash',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Створка'),
        ),
        migrations.AlterField(
            model_name='constructor',
            name='shtapik',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Штапик'),
        ),
    ]
