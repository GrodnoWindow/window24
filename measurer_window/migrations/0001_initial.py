# Generated by Django 4.1.2 on 2023-03-07 16:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Casing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Название')),
                ('price_in_currency', models.FloatField(blank=True, null=True, verbose_name='Цена EUR/USD')),
                ('price_in_byn', models.FloatField(blank=True, null=True, verbose_name='Цена BYN')),
            ],
            options={
                'verbose_name': 'Наличник',
                'verbose_name_plural': 'наличники',
            },
        ),
        migrations.CreateModel(
            name='Flashing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Название')),
                ('price_in_currency', models.FloatField(blank=True, null=True, verbose_name='Цена EUR/USD')),
                ('price_in_byn', models.FloatField(blank=True, null=True, verbose_name='Цена BYN')),
            ],
            options={
                'verbose_name': 'Нащельник',
                'verbose_name_plural': 'Нащельники',
            },
        ),
        migrations.CreateModel(
            name='InternalSlopes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Название')),
                ('price_in_currency', models.FloatField(blank=True, null=True, verbose_name='Цена EUR/USD')),
                ('price_in_byn', models.FloatField(blank=True, null=True, verbose_name='Цена BYN')),
            ],
            options={
                'verbose_name': 'Внутренние откосы',
                'verbose_name_plural': 'Внутренние откосы',
            },
        ),
        migrations.CreateModel(
            name='LowTides',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Название')),
                ('price_in_currency', models.FloatField(blank=True, null=True, verbose_name=' Цена EUR/USD')),
                ('price_in_byn', models.FloatField(blank=True, null=True, verbose_name='Цена BYN')),
            ],
            options={
                'verbose_name': 'Отлив',
                'verbose_name_plural': 'Отливы',
            },
        ),
        migrations.CreateModel(
            name='MountingMaterials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Название')),
                ('price_in_currency', models.FloatField(blank=True, null=True, verbose_name='Цена EUR/USD')),
                ('price_in_byn', models.FloatField(blank=True, null=True, verbose_name='Цена BYN')),
            ],
            options={
                'verbose_name': 'Монтажные материалы',
                'verbose_name_plural': 'Монтажные материалы',
            },
        ),
        migrations.CreateModel(
            name='SlopesOfMetal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Название')),
                ('price_in_currency', models.FloatField(blank=True, null=True, verbose_name='Цена EUR/USD')),
                ('price_in_byn', models.FloatField(blank=True, null=True, verbose_name='Цена BYN')),
            ],
            options={
                'verbose_name': 'Откосы из металла',
                'verbose_name_plural': 'Откосы из металла',
            },
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Статус')),
            ],
            options={
                'verbose_name': 'Статус',
                'verbose_name_plural': 'Статусы',
            },
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Единица измерия')),
            ],
            options={
                'verbose_name': 'Единица измерения',
                'verbose_name_plural': 'Единица измерения',
            },
        ),
        migrations.CreateModel(
            name='Visors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Название')),
                ('price_in_currency', models.FloatField(blank=True, null=True, verbose_name='Цена EUR/USD')),
                ('price_in_byn', models.FloatField(blank=True, null=True, verbose_name='Цена BYN')),
            ],
            options={
                'verbose_name': 'Козырек',
                'verbose_name_plural': 'козырьки',
            },
        ),
        migrations.CreateModel(
            name='Windowsill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Название')),
                ('price_in_currency', models.FloatField(blank=True, null=True, verbose_name=' Цена EUR/USD')),
                ('price_in_byn', models.FloatField(blank=True, null=True, verbose_name='Цена BYN')),
                ('unit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='measurer_window.unit', verbose_name='Единица измерения')),
            ],
            options={
                'verbose_name': 'Подоконник',
                'verbose_name_plural': 'Подоконники',
            },
        ),
        migrations.CreateModel(
            name='WindowsillWidth',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Полка подоконника')),
            ],
            options={
                'verbose_name': 'Полка подоконника',
                'verbose_name_plural': 'Полки подоконников',
            },
        ),
        migrations.CreateModel(
            name='WindowsillComplectCalc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.IntegerField(blank=True, null=True, verbose_name='Номер замера')),
                ('count', models.IntegerField(default=0, verbose_name='Количество')),
                ('price_in_byn', models.FloatField(default=0.0, max_length=255, verbose_name='Цена BYN')),
                ('price_in_currency', models.FloatField(default=0.0, max_length=255, verbose_name='Цена EUR/USD')),
                ('windowsill', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='measurer_window.windowsill', verbose_name='Комплектующие подоконника')),
            ],
            options={
                'verbose_name': 'Просчет комплектующих подоконников',
                'verbose_name_plural': 'Просчеты комплектующих подоконника',
            },
        ),
        migrations.CreateModel(
            name='WindowsillCalc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.IntegerField(blank=True, null=True, verbose_name='Номер замера')),
                ('length', models.IntegerField(default=0, verbose_name='Длинна')),
                ('count', models.IntegerField(default=0, verbose_name='Количество')),
                ('square_meter', models.FloatField(default=0.0, max_length=255, verbose_name='В метрах квадратных')),
                ('linear_meter', models.FloatField(default=0.0, max_length=255, verbose_name='В метрах погонных')),
                ('price_in_byn', models.FloatField(default=0.0, max_length=255, verbose_name='Цена BYN')),
                ('price_in_currency', models.FloatField(default=0.0, max_length=255, verbose_name='Цена EUR/USD')),
                ('windowsill', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='measurer_window.windowsill', verbose_name='Подоконник')),
                ('windowsill_width', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='measurer_window.windowsillwidth', verbose_name='Полка подоконник')),
            ],
            options={
                'verbose_name': 'Просчет подоконника',
                'verbose_name_plural': 'Просчеты подоконников',
            },
        ),
        migrations.CreateModel(
            name='VisorsCalc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.IntegerField(blank=True, null=True, verbose_name='Номер замера')),
                ('width', models.IntegerField(default=0, verbose_name='Ширина')),
                ('length', models.IntegerField(default=0, verbose_name='Длинна')),
                ('count', models.IntegerField(default=0, verbose_name='Количество')),
                ('square_meter', models.FloatField(default=0.0, max_length=255, verbose_name='В метрах квадратных')),
                ('linear_meter', models.FloatField(default=0.0, max_length=255, verbose_name='В метрах погонных')),
                ('price_in_byn', models.FloatField(default=0.0, max_length=255, verbose_name='Цена BYN')),
                ('price_in_currency', models.FloatField(default=0.0, max_length=255, verbose_name='Цена EUR/USD')),
                ('visors', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='measurer_window.visors', verbose_name='Козырек')),
            ],
            options={
                'verbose_name': 'Просчет козырька',
                'verbose_name_plural': 'Просчеты козырьков',
            },
        ),
        migrations.CreateModel(
            name='SlopesOfMetalCalc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.IntegerField(blank=True, null=True, verbose_name='Номер замера')),
                ('width', models.IntegerField(default=0, verbose_name='Ширина')),
                ('length', models.IntegerField(default=0, verbose_name='Длинна')),
                ('count', models.IntegerField(default=0, verbose_name='Количество')),
                ('square_meter', models.FloatField(default=0.0, max_length=255, verbose_name='В метрах квадратных')),
                ('linear_meter', models.FloatField(default=0.0, max_length=255, verbose_name='В метрах погонных')),
                ('price_in_byn', models.FloatField(default=0.0, max_length=255, verbose_name='Цена BYN')),
                ('price_in_currency', models.FloatField(default=0.0, max_length=255, verbose_name='Цена EUR/USD')),
                ('slopes_of_metal', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='measurer_window.slopesofmetal', verbose_name='Откосы из металла')),
            ],
            options={
                'verbose_name': 'Просчет откосов из металла',
                'verbose_name_plural': 'Просчеты откосов из металла',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(blank=True, max_length=255, null=True, verbose_name='Адрес')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Имя заказчика')),
                ('phone', models.CharField(blank=True, max_length=255, null=True, verbose_name='Номер телефона')),
                ('date', models.DateField(verbose_name='Дата замера')),
                ('sum_in_byn', models.FloatField(default=0.0, verbose_name='Сумма просчета BYN')),
                ('sum_in_currency', models.FloatField(default=0.0, verbose_name='Сумма просчета в EUR/USD')),
                ('status', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='measurer_window.status', verbose_name='статус')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Замерщик')),
                ('windowsill_calc', models.ManyToManyField(blank=True, to='measurer_window.windowsillcalc', verbose_name='Просчеты подоконников')),
            ],
            options={
                'verbose_name': 'Замер',
                'verbose_name_plural': 'Замеры',
            },
        ),
        migrations.CreateModel(
            name='MountingMaterialsCalc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.IntegerField(blank=True, null=True, verbose_name='Номер замера')),
                ('count', models.IntegerField(default=0, verbose_name='Количество')),
                ('price_in_byn', models.FloatField(default=0.0, max_length=255, verbose_name='Цена BYN')),
                ('price_in_currency', models.FloatField(default=0.0, max_length=255, verbose_name='Цена EUR/USD')),
                ('mounting_materials', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='measurer_window.mountingmaterials', verbose_name='Монтажные материалы')),
            ],
            options={
                'verbose_name': 'Просчет монтажных материалов',
                'verbose_name_plural': 'Просчеты внутренних монтажных материалов',
            },
        ),
        migrations.CreateModel(
            name='LowTidesComplectCalc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.IntegerField(blank=True, null=True, verbose_name='Номер замера')),
                ('count', models.IntegerField(default=0, verbose_name='Количество')),
                ('price_in_byn', models.FloatField(default=0.0, max_length=255, verbose_name='Цена BYN')),
                ('price_in_currency', models.FloatField(default=0.0, max_length=255, verbose_name='Цена EUR/USD')),
                ('low_tides', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='measurer_window.lowtides', verbose_name='Комплектующие отлива')),
            ],
            options={
                'verbose_name': 'Просчет комплектующих отливов',
                'verbose_name_plural': 'Просчеты комплектующих отливов',
            },
        ),
        migrations.CreateModel(
            name='LowTidesCalc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.IntegerField(blank=True, null=True, verbose_name='Номер замера')),
                ('width', models.IntegerField(default=0, verbose_name='Ширина')),
                ('length', models.IntegerField(default=0, verbose_name='Длинна')),
                ('count', models.IntegerField(default=0, verbose_name='Количество')),
                ('square_meter', models.FloatField(default=0.0, max_length=255, verbose_name='В метрах квадратных')),
                ('linear_meter', models.FloatField(default=0.0, max_length=255, verbose_name='В метрах погонных')),
                ('price_in_byn', models.FloatField(default=0.0, max_length=255, verbose_name='Цена BYN')),
                ('price_in_currency', models.FloatField(default=0.0, max_length=255, verbose_name='Цена EUR/USD')),
                ('low_tides', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='measurer_window.lowtides', verbose_name='Отлив')),
            ],
            options={
                'verbose_name': 'Просчет отлива',
                'verbose_name_plural': 'Просчеты отливов',
            },
        ),
        migrations.AddField(
            model_name='lowtides',
            name='unit',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='measurer_window.unit', verbose_name='Единица измерения'),
        ),
        migrations.CreateModel(
            name='InternalSlopesCalc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.IntegerField(blank=True, null=True, verbose_name='Номер замера')),
                ('width', models.IntegerField(default=0, verbose_name='Ширина')),
                ('length', models.IntegerField(default=0, verbose_name='Длинна')),
                ('count', models.IntegerField(default=0, verbose_name='Количество')),
                ('square_meter', models.FloatField(default=0.0, max_length=255, verbose_name='В метрах квадратных')),
                ('linear_meter', models.FloatField(default=0.0, max_length=255, verbose_name='В метрах погонных')),
                ('price_in_byn', models.FloatField(default=0.0, max_length=255, verbose_name='Цена BYN')),
                ('price_in_currency', models.FloatField(default=0.0, max_length=255, verbose_name='Цена EUR/USD')),
                ('internal_slopes', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='measurer_window.internalslopes', verbose_name='Внутренние откосы')),
            ],
            options={
                'verbose_name': 'Просчет внутренних откосов',
                'verbose_name_plural': 'Просчеты внутренних откосов',
            },
        ),
        migrations.CreateModel(
            name='FlashingCalc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.IntegerField(blank=True, null=True, verbose_name='Номер замера')),
                ('width', models.IntegerField(default=0, verbose_name='Ширина')),
                ('length', models.IntegerField(default=0, verbose_name='Длинна')),
                ('count', models.IntegerField(default=0, verbose_name='Количество')),
                ('square_meter', models.FloatField(default=0.0, max_length=255, verbose_name='В метрах квадратных')),
                ('linear_meter', models.FloatField(default=0.0, max_length=255, verbose_name='В метрах погонных')),
                ('price_in_byn', models.FloatField(default=0.0, max_length=255, verbose_name='Цена BYN')),
                ('price_in_currency', models.FloatField(default=0.0, max_length=255, verbose_name='Цена EUR/USD')),
                ('flashing', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='measurer_window.flashing', verbose_name='Нащельник')),
            ],
            options={
                'verbose_name': 'Просчет нащельника',
                'verbose_name_plural': 'Просчеты нащельников',
            },
        ),
        migrations.CreateModel(
            name='CasingCalc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.IntegerField(blank=True, null=True, verbose_name='Номер замера')),
                ('width', models.IntegerField(default=0, verbose_name='Ширина')),
                ('length', models.IntegerField(default=0, verbose_name='Длинна')),
                ('count', models.IntegerField(default=0, verbose_name='Количество')),
                ('square_meter', models.FloatField(default=0.0, max_length=255, verbose_name='В метрах квадратных')),
                ('linear_meter', models.FloatField(default=0.0, max_length=255, verbose_name='В метрах погонных')),
                ('price_in_byn', models.FloatField(default=0.0, max_length=255, verbose_name='Цена BYN')),
                ('price_in_currency', models.FloatField(default=0.0, max_length=255, verbose_name='Цена EUR/USD')),
                ('casing', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='measurer_window.casing', verbose_name='Наличник')),
            ],
            options={
                'verbose_name': 'Просчет наличника',
                'verbose_name_plural': 'Просчеты наличников',
            },
        ),
    ]
