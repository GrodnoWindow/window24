# Generated by Django 4.1.2 on 2023-02-08 05:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('constructor', '0002_casing_provider_flashing_provider_lowtides_provider_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CasingCalc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('casing_id', models.IntegerField(blank=True, default=0.0, null=True, verbose_name='№ Наличник')),
                ('markups_type', models.CharField(max_length=255, verbose_name='Наценка ')),
                ('width', models.FloatField(default=0.0, max_length=255, verbose_name='Ширина')),
                ('length', models.FloatField(default=0.0, max_length=255, verbose_name='Длинна')),
                ('count', models.FloatField(default=0.0, max_length=255, verbose_name='Количество')),
                ('linear_meter', models.FloatField(default=0.0, max_length=255, verbose_name='В метрах погонных')),
                ('square_meter', models.FloatField(default=0.0, max_length=255, verbose_name='В метрах квадратных')),
                ('price_output', models.FloatField(default=0.0, max_length=255, verbose_name='Цена')),
            ],
            options={
                'verbose_name': 'Просчет наличника',
                'verbose_name_plural': 'Просчеты наличников',
            },
        ),
        migrations.CreateModel(
            name='ExchangeRates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Имя')),
                ('value', models.FloatField(default=0.0, max_length=255, verbose_name='Значение')),
                ('auto', models.BooleanField(default=True, verbose_name='Получать автоматически')),
                ('add_percent', models.BooleanField(default=False, verbose_name='Добавлять в процентах')),
                ('value_percent', models.FloatField(default=0.0, max_length=255, verbose_name='Значение в процентах')),
            ],
            options={
                'verbose_name': 'Курс валют',
                'verbose_name_plural': 'Курсы валют',
            },
        ),
        migrations.CreateModel(
            name='FlashingCalc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flashing_id', models.IntegerField(blank=True, default=0.0, null=True, verbose_name='№ Нащельника')),
                ('markups_type', models.CharField(max_length=255, verbose_name='Наценка ')),
                ('width', models.FloatField(default=0.0, max_length=255, verbose_name='Ширина')),
                ('length', models.FloatField(default=0.0, max_length=255, verbose_name='Длинна')),
                ('count', models.FloatField(default=0.0, max_length=255, verbose_name='Количество')),
                ('linear_meter', models.FloatField(default=0.0, max_length=255, verbose_name='В метрах погонных')),
                ('square_meter', models.FloatField(default=0.0, max_length=255, verbose_name='В метрах квадратных')),
                ('price_output', models.FloatField(default=0.0, max_length=255, verbose_name='Цена')),
            ],
            options={
                'verbose_name': 'Просчет нащельника',
                'verbose_name_plural': 'Просчеты нащельников',
            },
        ),
        migrations.CreateModel(
            name='LowTidesCalc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('low_tides_id', models.IntegerField(blank=True, default=0.0, null=True, verbose_name='№ Отлив')),
                ('markups_type', models.CharField(max_length=255, verbose_name='Наценка ')),
                ('width', models.FloatField(default=0.0, max_length=255, verbose_name='Ширина')),
                ('length', models.FloatField(default=0.0, max_length=255, verbose_name='Длинна')),
                ('count', models.FloatField(default=0.0, max_length=255, verbose_name='количество')),
                ('linear_meter', models.FloatField(default=0.0, max_length=255, verbose_name='В метрах погонных')),
                ('square_meter', models.FloatField(default=0.0, max_length=255, verbose_name='В метрах квадратных')),
                ('price_output', models.FloatField(default=0.0, max_length=255, verbose_name='цена')),
            ],
            options={
                'verbose_name': 'Просчет отлива',
                'verbose_name_plural': 'Просчеты отливов',
            },
        ),
        migrations.CreateModel(
            name='Markups',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('low_tides', models.FloatField(default=0.0, max_length=255, verbose_name='Отливы ')),
                ('low_tides_in_percent', models.BooleanField(default=True, verbose_name='считать в процентах отливы')),
                ('window', models.FloatField(default=0.0, max_length=255, verbose_name='Окна')),
                ('window_in_percent', models.BooleanField(default=True, verbose_name='считать в процентах окно')),
            ],
            options={
                'verbose_name': 'Наценки',
                'verbose_name_plural': 'Наценки',
            },
        ),
        migrations.CreateModel(
            name='VisorsCalc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visors_id', models.IntegerField(blank=True, default=0.0, null=True, verbose_name='№ Козырька')),
                ('markups_type', models.CharField(max_length=255, verbose_name='Наценка ')),
                ('width', models.FloatField(default=0.0, max_length=255, verbose_name='Ширина')),
                ('length', models.FloatField(default=0.0, max_length=255, verbose_name='Длинна')),
                ('count', models.FloatField(default=0.0, max_length=255, verbose_name='Количество')),
                ('linear_meter', models.FloatField(default=0.0, max_length=255, verbose_name='В метрах погонных')),
                ('square_meter', models.FloatField(default=0.0, max_length=255, verbose_name='В метрах квадратных')),
                ('price_output', models.FloatField(default=0.0, max_length=255, verbose_name='Цена')),
            ],
            options={
                'verbose_name': 'Просчет наличника',
                'verbose_name_plural': 'Просчеты наличников',
            },
        ),
        migrations.CreateModel(
            name='WindowsCalc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discount', models.FloatField(blank=True, max_length=255, null=True, verbose_name='Скидка на окно')),
                ('profile_id', models.IntegerField(blank=True, null=True, verbose_name='Профиль id')),
                ('fittings_id', models.IntegerField(blank=True, null=True, verbose_name='Фурнитура id ')),
                ('currency_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Валюта имя')),
                ('currency_value', models.FloatField(blank=True, max_length=255, null=True, verbose_name='Валюта значение НБРБ')),
                ('price_input', models.FloatField(default=0.0, max_length=255, verbose_name='Входная цена')),
                ('price_output', models.FloatField(default=0.0, max_length=255, verbose_name='Выходная цена ( с наценкой )')),
                ('markup_type', models.IntegerField(blank=True, null=True, verbose_name='Тип наценки')),
                ('markup_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Название наценки')),
                ('markup_value', models.FloatField(default=0.0, max_length=255, verbose_name='Значение наценки')),
                ('markup_percent', models.BooleanField(default=True, verbose_name='Наценка в процентах')),
            ],
            options={
                'verbose_name': 'Просчет окна',
                'verbose_name_plural': 'Просчеты окон',
            },
        ),
        migrations.CreateModel(
            name='WindowsillCalc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('windowsill_id', models.IntegerField(blank=True, default=0.0, null=True, verbose_name='№ Подоконник')),
                ('plug', models.IntegerField(blank=True, default=0, null=True, verbose_name='Заглушка')),
                ('connector', models.IntegerField(blank=True, default=0, null=True, verbose_name='Соединитель')),
                ('markups_type', models.CharField(max_length=255, verbose_name='Наценка')),
                ('width', models.FloatField(default=0.0, max_length=255, verbose_name='Ширина')),
                ('length', models.FloatField(default=0.0, max_length=255, verbose_name='Длинна')),
                ('count', models.FloatField(default=0.0, max_length=255, verbose_name='Количество')),
                ('square_meter', models.FloatField(default=0.0, max_length=255, verbose_name='В метрах квадратных')),
                ('linear_meter', models.FloatField(default=0.0, max_length=255, verbose_name='В метрах погонных')),
                ('price_output', models.FloatField(default=0.0, max_length=255, verbose_name='Цена')),
            ],
            options={
                'verbose_name': 'Просчет подоконника',
                'verbose_name_plural': 'Просчеты подоконников',
            },
        ),
        migrations.CreateModel(
            name='Windowsill_Markups',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('markups_diler', models.FloatField(default=0.0, max_length=255, verbose_name='Наценка диллерская')),
                ('markups_diler_in_percent', models.BooleanField(default=True, verbose_name='Добавлять в процентах ( диллер )')),
                ('markups_retail', models.FloatField(default=0.0, max_length=255, verbose_name='Наценка розничная')),
                ('markups_retail_in_percent', models.BooleanField(default=True, verbose_name='Добавлять в процентах ( розница )')),
                ('markups_3', models.FloatField(default=0.0, max_length=255, verbose_name='Наценка №3')),
                ('markups_3_in_percent', models.BooleanField(default=True, verbose_name='Добавлять в процентах ( наценка №3 )')),
                ('markups_4', models.FloatField(default=0.0, max_length=255, verbose_name='Наценка №4')),
                ('markups_4_in_percent', models.BooleanField(default=True, verbose_name='Добавлять в процентах ( наценка №4 )')),
                ('markups_5', models.FloatField(default=0.0, max_length=255, verbose_name='Наценка №5')),
                ('markups_5_in_percent', models.BooleanField(default=True, verbose_name='Добавлять в процентах ( наценка №5 )')),
                ('windowsill', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='constructor.windowsill', verbose_name='Подоконник')),
            ],
            options={
                'verbose_name': 'Наценка на подоконник',
                'verbose_name_plural': 'Наценка на подоконники',
            },
        ),
        migrations.CreateModel(
            name='WindowDiscountMarkups',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discount', models.FloatField(default=0.0, max_length=255, verbose_name='Значение')),
                ('markups_diler', models.FloatField(default=0.0, max_length=255, verbose_name='Наценка диллерская')),
                ('markups_diler_in_percent', models.BooleanField(default=True, verbose_name='Добавлять в процентах ( диллер )')),
                ('markups_retail', models.FloatField(default=0.0, max_length=255, verbose_name='Наценка розничная')),
                ('markups_retail_in_percent', models.BooleanField(default=True, verbose_name='Добавлять в процентах ( розница )')),
                ('markups_3', models.FloatField(default=0.0, max_length=255, verbose_name='Наценка №3')),
                ('markups_3_in_percent', models.BooleanField(default=True, verbose_name='Добавлять в процентах ( наценка №3 )')),
                ('markups_4', models.FloatField(default=0.0, max_length=255, verbose_name='Наценка №4')),
                ('markups_4_in_percent', models.BooleanField(default=True, verbose_name='Добавлять в процентах ( наценка №4 )')),
                ('markups_5', models.FloatField(default=0.0, max_length=255, verbose_name='Наценка №5')),
                ('markups_5_in_percent', models.BooleanField(default=True, verbose_name='Добавлять в процентах ( наценка №5 )')),
                ('fittings_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='constructor.fittings', verbose_name='Фурнитура')),
                ('profile_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='constructor.profile', verbose_name='Профиль')),
            ],
            options={
                'verbose_name': 'Скидка/Наценка на окно',
                'verbose_name_plural': 'Скидки/Наценки на окна',
            },
        ),
        migrations.CreateModel(
            name='Visors_Markups',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('markups_diler', models.FloatField(default=0.0, max_length=255, verbose_name='Наценка диллерская')),
                ('markups_diler_in_percent', models.BooleanField(default=True, verbose_name='Добавлять в процентах ( диллер )')),
                ('markups_retail', models.FloatField(default=0.0, max_length=255, verbose_name='Наценка розничная')),
                ('markups_retail_in_percent', models.BooleanField(default=True, verbose_name='Добавлять в процентах ( розница )')),
                ('markups_3', models.FloatField(default=0.0, max_length=255, verbose_name='Наценка №3')),
                ('markups_3_in_percent', models.BooleanField(default=True, verbose_name='Добавлять в процентах ( наценка №3 )')),
                ('markups_4', models.FloatField(default=0.0, max_length=255, verbose_name='Наценка №4')),
                ('markups_4_in_percent', models.BooleanField(default=True, verbose_name='Добавлять в процентах ( наценка №4 )')),
                ('markups_5', models.FloatField(default=0.0, max_length=255, verbose_name='Наценка №5')),
                ('markups_5_in_percent', models.BooleanField(default=True, verbose_name='Добавлять в процентах ( наценка №5 )')),
                ('visors', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='constructor.visors', verbose_name='Козырек')),
            ],
            options={
                'verbose_name': 'Наценка на козырек',
                'verbose_name_plural': 'Наценка на козырьки',
            },
        ),
        migrations.CreateModel(
            name='LowTides_Markups',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('markups_diler', models.FloatField(default=0.0, max_length=255, verbose_name='Наценка диллерская')),
                ('markups_diler_in_percent', models.BooleanField(default=True, verbose_name='Добавлять в процентах ( диллер )')),
                ('markups_retail', models.FloatField(default=0.0, max_length=255, verbose_name='Наценка розничная')),
                ('markups_retail_in_percent', models.BooleanField(default=True, verbose_name='Добавлять в процентах ( розница )')),
                ('markups_3', models.FloatField(default=0.0, max_length=255, verbose_name='Наценка №3')),
                ('markups_3_in_percent', models.BooleanField(default=True, verbose_name='Добавлять в процентах ( наценка №3 )')),
                ('markups_4', models.FloatField(default=0.0, max_length=255, verbose_name='Наценка №4')),
                ('markups_4_in_percent', models.BooleanField(default=True, verbose_name='Добавлять в процентах ( наценка №4 )')),
                ('markups_5', models.FloatField(default=0.0, max_length=255, verbose_name='Наценка №5')),
                ('markups_5_in_percent', models.BooleanField(default=True, verbose_name='Добавлять в процентах ( наценка №5 )')),
                ('lowtides', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='constructor.lowtides', verbose_name='Отливы')),
            ],
            options={
                'verbose_name': 'Наценка на отлив',
                'verbose_name_plural': 'Наценка на отливы',
            },
        ),
        migrations.CreateModel(
            name='Flashing_Markups',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('markups_diler', models.FloatField(default=0.0, max_length=255, verbose_name='Наценка диллерская')),
                ('markups_diler_in_percent', models.BooleanField(default=True, verbose_name='Добавлять в процентах ( диллер )')),
                ('markups_retail', models.FloatField(default=0.0, max_length=255, verbose_name='Наценка розничная')),
                ('markups_retail_in_percent', models.BooleanField(default=True, verbose_name='Добавлять в процентах ( розница )')),
                ('markups_3', models.FloatField(default=0.0, max_length=255, verbose_name='Наценка №3')),
                ('markups_3_in_percent', models.BooleanField(default=True, verbose_name='Добавлять в процентах ( наценка №3 )')),
                ('markups_4', models.FloatField(default=0.0, max_length=255, verbose_name='Наценка №4')),
                ('markups_4_in_percent', models.BooleanField(default=True, verbose_name='Добавлять в процентах ( наценка №4 )')),
                ('markups_5', models.FloatField(default=0.0, max_length=255, verbose_name='Наценка №5')),
                ('markups_5_in_percent', models.BooleanField(default=True, verbose_name='Добавлять в процентах ( наценка №5 )')),
                ('flashing', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='constructor.flashing', verbose_name='Нащельник')),
            ],
            options={
                'verbose_name': 'Наценка на нащельник',
                'verbose_name_plural': 'Наценка на нащельники',
            },
        ),
        migrations.CreateModel(
            name='Constructor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price_constructor', models.FloatField(blank=True, default=0.0, max_length=255, null=True, verbose_name='Цена всего просчета')),
                ('additional_profile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='constructor.additionalprofile', verbose_name='Доборные профиля')),
                ('aggregate', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='constructor.aggregate', verbose_name='Заполнитель')),
                ('casing_calc', models.ManyToManyField(blank=True, to='calculation.casingcalc', verbose_name='Просчеты наличников')),
                ('connection_profile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='constructor.connectionprofile', verbose_name='Соединительные профиля')),
                ('door', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='constructor.door', verbose_name='Двери')),
                ('flashing_calc', models.ManyToManyField(blank=True, to='calculation.flashingcalc', verbose_name='Просчеты нащельников')),
                ('gorbylki', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='constructor.gorbylki', verbose_name='Горбыльки')),
                ('handles', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='constructor.handles', verbose_name='Ручки')),
                ('lamination', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='constructor.lamination', verbose_name='Ламинация')),
                ('lowtides_calc', models.ManyToManyField(blank=True, to='calculation.lowtidescalc', verbose_name='Просчеты отливов')),
                ('other_complectation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='constructor.othercomplectation', verbose_name='Прочее комплектующие')),
                ('product_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='constructor.producttype', verbose_name='Тип изделия')),
                ('sash', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='constructor.sash', verbose_name='Створка')),
                ('sealant', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='constructor.sealant', verbose_name='Уплотнитель')),
                ('shtapik', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='constructor.shtapik', verbose_name='Штапик')),
                ('visors_calc', models.ManyToManyField(blank=True, to='calculation.visorscalc', verbose_name='Просчеты козырьков')),
                ('window_calc', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='calculation.windowscalc', verbose_name='Просчет окна')),
                ('windowsills_calc', models.ManyToManyField(blank=True, to='calculation.windowsillcalc', verbose_name='Просчеты подоконников')),
                ('works', models.ManyToManyField(blank=True, to='constructor.works', verbose_name='Работы')),
            ],
            options={
                'verbose_name': 'Просчет конструктора',
                'verbose_name_plural': 'Просчеты конструкторов',
            },
        ),
        migrations.CreateModel(
            name='Casing_Markups',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('markups_diler', models.FloatField(default=0.0, max_length=255, verbose_name='Наценка диллерская')),
                ('markups_diler_in_percent', models.BooleanField(default=True, verbose_name='Добавлять в процентах ( диллер )')),
                ('markups_retail', models.FloatField(default=0.0, max_length=255, verbose_name='Наценка розничная')),
                ('markups_retail_in_percent', models.BooleanField(default=True, verbose_name='Добавлять в процентах ( розница )')),
                ('markups_3', models.FloatField(default=0.0, max_length=255, verbose_name='Наценка №3')),
                ('markups_3_in_percent', models.BooleanField(default=True, verbose_name='Добавлять в процентах ( наценка №3 )')),
                ('markups_4', models.FloatField(default=0.0, max_length=255, verbose_name='Наценка №4')),
                ('markups_4_in_percent', models.BooleanField(default=True, verbose_name='Добавлять в процентах ( наценка №4 )')),
                ('markups_5', models.FloatField(default=0.0, max_length=255, verbose_name='Наценка №5')),
                ('markups_5_in_percent', models.BooleanField(default=True, verbose_name='Добавлять в процентах ( наценка №5 )')),
                ('casing', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='constructor.casing', verbose_name='Наличник')),
            ],
            options={
                'verbose_name': 'Наценка на наличник',
                'verbose_name_plural': 'Наценка на наличники',
            },
        ),
    ]
