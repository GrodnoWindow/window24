# Generated by Django 4.1.2 on 2022-12-19 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('call', '0001_initial'),
        ('complaint', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Number',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(blank=True, max_length=255)),
                ('name', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Prompter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_select', models.IntegerField(blank=True, null=True, verbose_name='Категория выбора')),
                ('main_statements', models.CharField(blank=True, max_length=255, verbose_name='Основные высказывания')),
                ('type_home', models.IntegerField(blank=True, null=True, verbose_name='Тип дома')),
                ('built_from', models.IntegerField(blank=True, null=True, verbose_name='Из чего построен')),
                ('sun_heating', models.BooleanField(blank=True, default=False, verbose_name='Летом солнце нагревает')),
                ('weak_light', models.BooleanField(blank=True, default=False, verbose_name='Мало света ')),
                ('noise_outside', models.BooleanField(blank=True, default=False, verbose_name='Шум за окном')),
                ('winter_cold', models.BooleanField(blank=True, default=False, verbose_name='Зимой холодно')),
                ('rose_of_wind', models.BooleanField(blank=True, default=False, verbose_name='Роза ветров')),
                ('children', models.BooleanField(blank=True, default=False, verbose_name='Есть ли дети')),
                ('installation_room', models.IntegerField(blank=True, null=True, verbose_name='Комната установки')),
                ('special_offers', models.CharField(blank=True, max_length=255, verbose_name='Специальные предложения')),
                ('solution_window', models.CharField(blank=True, max_length=255, verbose_name='Почему решили поменять окно')),
                ('only_window', models.BooleanField(blank=True, default=False, verbose_name='Только окно')),
                ('mounting_all', models.IntegerField(blank=True, null=True, verbose_name='Монтаж отливов/подоконников')),
                ('slopes', models.BooleanField(blank=True, default=False, verbose_name='Отделка откосов')),
                ('mosquito_net', models.BooleanField(blank=True, default=False, verbose_name='Москитная сетка')),
                ('room', models.CharField(blank=True, max_length=255, verbose_name='В какую комнату установка')),
                ('individual_wishes', models.CharField(blank=True, max_length=255, verbose_name='Индивидуальные пожелания')),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(blank=True, max_length=255)),
                ('name', models.CharField(blank=True, max_length=255)),
                ('time_created', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
                ('addresses', models.ManyToManyField(blank=True, to='client.address')),
                ('calls', models.ManyToManyField(blank=True, to='call.call')),
                ('complaints', models.ManyToManyField(blank=True, to='complaint.complaint', verbose_name='Жалобы')),
            ],
        ),
    ]
