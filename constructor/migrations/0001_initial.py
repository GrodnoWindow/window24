# Generated by Django 4.1.2 on 2022-12-19 22:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Accessories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Комлпектующие')),
            ],
            options={
                'verbose_name': 'Комлпектующие',
                'verbose_name_plural': 'Комлпектующие',
            },
        ),
        migrations.CreateModel(
            name='Aggregate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Заполнитель №1')),
            ],
            options={
                'verbose_name': 'Заполнитель №1',
                'verbose_name_plural': 'Заполнитель №1',
            },
        ),
        migrations.CreateModel(
            name='BayWindowToProfile60',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Эркер к профилю 60мм')),
            ],
            options={
                'verbose_name': 'Эркер к профилю 60мм',
                'verbose_name_plural': 'Эркер к профилю 60мм',
            },
        ),
        migrations.CreateModel(
            name='BayWindowToProfile70',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Эркер к профилю 70мм')),
            ],
            options={
                'verbose_name': 'Эркер к профилю 70мм',
                'verbose_name_plural': 'Эркер к профилю 70мм',
            },
        ),
        migrations.CreateModel(
            name='Connector90g',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Соединитель 90гр')),
            ],
            options={
                'verbose_name': 'Соединитель 90гр',
                'verbose_name_plural': 'Соединитель 90гр',
            },
        ),
        migrations.CreateModel(
            name='ExtensionsToProfile60',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Доборы к профилю 60мм')),
            ],
            options={
                'verbose_name': 'Доборы к профилю 60мм',
                'verbose_name_plural': 'Доборы к профилю 60мм',
            },
        ),
        migrations.CreateModel(
            name='ExtensionsToProfile70',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Доборы к профилю 70мм')),
            ],
            options={
                'verbose_name': 'Доборы к профилю 70мм',
                'verbose_name_plural': 'Доборы к профилю 70мм',
            },
        ),
        migrations.CreateModel(
            name='FavoritePositions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Избранные позиции')),
            ],
            options={
                'verbose_name': 'Избранные позиции',
                'verbose_name_plural': 'Избранные позиции',
            },
        ),
        migrations.CreateModel(
            name='Fittings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Фурнитура')),
            ],
            options={
                'verbose_name': 'Фурнитура',
                'verbose_name_plural': 'Фурнитуры',
            },
        ),
        migrations.CreateModel(
            name='Flashing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Нащельник')),
            ],
            options={
                'verbose_name': 'Нащельник',
                'verbose_name_plural': 'Нащельник',
            },
        ),
        migrations.CreateModel(
            name='FlashingMetal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Нащельник Металл')),
            ],
            options={
                'verbose_name': 'Нащельник Металл',
                'verbose_name_plural': 'Нащельник Металл',
            },
        ),
        migrations.CreateModel(
            name='FreePositions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Бесплатные позиции')),
            ],
            options={
                'verbose_name': 'Бесплатные позиции',
                'verbose_name_plural': 'Бесплатные позиции',
            },
        ),
        migrations.CreateModel(
            name='Handles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Ручка')),
            ],
            options={
                'verbose_name': 'Ручка',
                'verbose_name_plural': 'Ручки',
            },
        ),
        migrations.CreateModel(
            name='LaminationInside',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Ланиманция внутри')),
            ],
            options={
                'verbose_name': 'Ланиманция внутри',
                'verbose_name_plural': 'Ланиманция внутри',
            },
        ),
        migrations.CreateModel(
            name='LaminationOutside',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Ламинация снаружи')),
            ],
            options={
                'verbose_name': 'Ламинация снаружи',
                'verbose_name_plural': 'Ламинация снаружи',
            },
        ),
        migrations.CreateModel(
            name='Locks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Замок')),
            ],
            options={
                'verbose_name': 'Замок',
                'verbose_name_plural': 'Замки',
            },
        ),
        migrations.CreateModel(
            name='LowTidesType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Тип отлива')),
            ],
            options={
                'verbose_name': 'Тип отлива',
                'verbose_name_plural': 'Типы отливов',
            },
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Примечание')),
            ],
            options={
                'verbose_name': 'Примечание',
                'verbose_name_plural': 'Примечание',
            },
        ),
        migrations.CreateModel(
            name='Platband',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Наличник')),
            ],
            options={
                'verbose_name': 'Наличник',
                'verbose_name_plural': 'Наличник',
            },
        ),
        migrations.CreateModel(
            name='ProductsInstall',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Монтаж изделий')),
            ],
            options={
                'verbose_name': 'Монтаж изделий',
                'verbose_name_plural': 'Монтаж изделий',
            },
        ),
        migrations.CreateModel(
            name='ProductType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Тип изделия')),
            ],
            options={
                'verbose_name': 'Тип изделия',
                'verbose_name_plural': 'Тип изделия',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Профиль')),
            ],
            options={
                'verbose_name': 'Профиль',
                'verbose_name_plural': 'Профили',
            },
        ),
        migrations.CreateModel(
            name='ProfileWeight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Масса профиля')),
            ],
            options={
                'verbose_name': 'Масса профиля',
                'verbose_name_plural': 'Масса профиля',
            },
        ),
        migrations.CreateModel(
            name='PvcSlopes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Откосы ПВХ')),
            ],
            options={
                'verbose_name': 'Откосы ПВХ',
                'verbose_name_plural': 'Откосы ПВХ',
            },
        ),
        migrations.CreateModel(
            name='Sash',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Створка')),
            ],
            options={
                'verbose_name': 'Створка',
                'verbose_name_plural': 'Створки',
            },
        ),
        migrations.CreateModel(
            name='SealColor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Цвет уплотнения')),
            ],
            options={
                'verbose_name': 'Цвет уплотнения',
                'verbose_name_plural': 'Цвет уплотнения',
            },
        ),
        migrations.CreateModel(
            name='SealInternal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Уплотнение внутренее')),
            ],
            options={
                'verbose_name': 'Уплотнение внутренее',
                'verbose_name_plural': 'Уплотнение внутренее',
            },
        ),
        migrations.CreateModel(
            name='SealOutside',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Уплотнение снаружи')),
            ],
            options={
                'verbose_name': 'Уплотнение снаружи',
                'verbose_name_plural': 'Уплотнение снаружи',
            },
        ),
        migrations.CreateModel(
            name='SealRebate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Уплотнение притвора')),
            ],
            options={
                'verbose_name': 'Уплотнение притвора',
                'verbose_name_plural': 'Уплотнение притвора',
            },
        ),
        migrations.CreateModel(
            name='Shpros',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Шпрос')),
            ],
            options={
                'verbose_name': 'Шпрос',
                'verbose_name_plural': 'Шпросы',
            },
        ),
        migrations.CreateModel(
            name='Shtapik',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Штапик')),
            ],
            options={
                'verbose_name': 'Штапик',
                'verbose_name_plural': 'Штапики',
            },
        ),
        migrations.CreateModel(
            name='StraightConnectors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Прямые соединители')),
            ],
            options={
                'verbose_name': 'Прямые соединители',
                'verbose_name_plural': 'Прямые соединители',
            },
        ),
        migrations.CreateModel(
            name='SupplyValve',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Приточный клапан')),
            ],
            options={
                'verbose_name': 'Приточный клапан',
                'verbose_name_plural': 'Приточные клапаны',
            },
        ),
        migrations.CreateModel(
            name='Visors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Козырьки')),
            ],
            options={
                'verbose_name': 'Козырьки',
                'verbose_name_plural': 'Козырьки',
            },
        ),
        migrations.CreateModel(
            name='WindowsillColor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Цвет подоконника')),
            ],
            options={
                'verbose_name': 'Цвет подоконника',
                'verbose_name_plural': 'Цвета подоконников',
            },
        ),
        migrations.CreateModel(
            name='WindowsillType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Тип подоконника')),
                ('type_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='windowsill_type')),
            ],
            options={
                'verbose_name': 'Тип подоконника',
                'verbose_name_plural': 'Тип подоконников',
            },
        ),
        migrations.CreateModel(
            name='Works',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Наименование работы')),
                ('price', models.FloatField(default=0.0, max_length=255, verbose_name='Цена работы')),
            ],
            options={
                'verbose_name': 'Просчет работы',
                'verbose_name_plural': 'Просчеты работ',
            },
        ),
        migrations.CreateModel(
            name='Windowsill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price_input', models.FloatField(blank=True, default=0.0, null=True, verbose_name='Цена закупки')),
                ('color', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='constructor.windowsillcolor', verbose_name='Цвет подоконника')),
                ('type', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='constructor.windowsilltype', verbose_name='Тип подоконника')),
            ],
            options={
                'verbose_name': 'Подоконник',
                'verbose_name_plural': 'Подоконники',
            },
        ),
        migrations.CreateModel(
            name='LowTides',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Название отлива')),
                ('price_input', models.FloatField(blank=True, default=0.0, null=True, verbose_name='Цена закупки')),
                ('type', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='constructor.lowtidestype', verbose_name='Тип отлива')),
            ],
            options={
                'verbose_name': 'Отлив',
                'verbose_name_plural': 'Отливы',
            },
        ),
    ]