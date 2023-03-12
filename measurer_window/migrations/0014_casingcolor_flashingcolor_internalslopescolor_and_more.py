# Generated by Django 4.1.2 on 2023-03-12 21:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('measurer_window', '0013_lowtidestype_alter_lowtidescalc_low_tides_connection_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CasingColor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Цвет наличника')),
            ],
            options={
                'verbose_name': 'Цвет наличника',
                'verbose_name_plural': 'Цвета наличников',
            },
        ),
        migrations.CreateModel(
            name='FlashingColor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Цвет нащельника')),
            ],
            options={
                'verbose_name': 'Цвет нащельника',
                'verbose_name_plural': 'Цвета нащельников',
            },
        ),
        migrations.CreateModel(
            name='InternalSlopesColor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Цвет внутренних откосов')),
            ],
            options={
                'verbose_name': 'Цвет внутренних откосов',
                'verbose_name_plural': 'Цвета внутренних откосов',
            },
        ),
        migrations.CreateModel(
            name='SlopesOfMetalColor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Цвет откосов из металла')),
            ],
            options={
                'verbose_name': 'Цвет откоса из металла',
                'verbose_name_plural': 'Цвета откосов из металла',
            },
        ),
        migrations.CreateModel(
            name='VisorsColor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Цвет козырька')),
            ],
            options={
                'verbose_name': 'Цвет козырька',
                'verbose_name_plural': 'Цвета козырьков',
            },
        ),
        migrations.AlterField(
            model_name='lowtidescalc',
            name='low_tides_count',
            field=models.IntegerField(default=0, verbose_name='Количество  отливов'),
        ),
        migrations.DeleteModel(
            name='LowTidesComplectCalc',
        ),
        migrations.AddField(
            model_name='casingcalc',
            name='casing_color',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='measurer_window.casingcolor', verbose_name='Цвет наличника'),
        ),
        migrations.AddField(
            model_name='flashingcalc',
            name='flashing_color',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='measurer_window.flashingcolor', verbose_name='Цвет нащельника'),
        ),
        migrations.AddField(
            model_name='internalslopescalc',
            name='internal_slopes_color',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='measurer_window.internalslopescolor', verbose_name='Цвет внутреннего откоса'),
        ),
        migrations.AddField(
            model_name='slopesofmetalcalc',
            name='slopes_of_metal_color',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='measurer_window.slopesofmetalcolor', verbose_name='Цвет откоса из метлла'),
        ),
        migrations.AddField(
            model_name='visorscalc',
            name='visors_color',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='measurer_window.visorscolor', verbose_name='Цвет козырька'),
        ),
    ]
