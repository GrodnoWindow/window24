# Generated by Django 4.1.2 on 2023-02-18 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('constructor', '0003_alter_profile_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='InternalSlope',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(blank=True, max_length=255, null=True, verbose_name='Тип внутренних откосов')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Наименование внутренних откосов')),
                ('color', models.CharField(blank=True, max_length=255, null=True, verbose_name='Цвет внутренних')),
                ('provider', models.CharField(blank=True, max_length=255, null=True, verbose_name='Поставщик')),
                ('price_input', models.FloatField(blank=True, default=0.0, null=True, verbose_name='Цена закупки')),
            ],
            options={
                'verbose_name': 'Внутренние откосы',
                'verbose_name_plural': 'Внутренние откосы',
            },
        ),
        migrations.CreateModel(
            name='MountingMaterials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(blank=True, max_length=255, null=True, verbose_name='Тип монтажных материалов')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Наименование монтажных материалов')),
                ('provider', models.CharField(blank=True, max_length=255, null=True, verbose_name='Поставщик')),
                ('price_input', models.FloatField(blank=True, default=0.0, null=True, verbose_name='Цена закупки')),
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
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Тип откосов из металла')),
                ('color', models.CharField(blank=True, max_length=255, null=True, verbose_name='Цвет откосов из металла')),
                ('provider', models.CharField(blank=True, max_length=255, null=True, verbose_name='Поставщик')),
                ('price_input', models.FloatField(blank=True, default=0.0, null=True, verbose_name='Цена закупки')),
            ],
            options={
                'verbose_name': 'Откосы из металла',
                'verbose_name_plural': 'откосы из металла',
            },
        ),
        migrations.DeleteModel(
            name='ExtensionsToProfile60',
        ),
        migrations.DeleteModel(
            name='FlashingMetal',
        ),
        migrations.DeleteModel(
            name='Platband',
        ),
        migrations.RemoveField(
            model_name='lowtides',
            name='type',
        ),
        migrations.RemoveField(
            model_name='visors',
            name='sweep',
        ),
        migrations.AddField(
            model_name='casing',
            name='color',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Цвет наличника'),
        ),
        migrations.AddField(
            model_name='flashing',
            name='color',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Цвет нащельника'),
        ),
        migrations.AddField(
            model_name='lowtides',
            name='color',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Цвет отлива'),
        ),
        migrations.AddField(
            model_name='visors',
            name='color',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Цвет козырька'),
        ),
        migrations.AddField(
            model_name='windowsill',
            name='color',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Цвет подоконника'),
        ),
        migrations.AddField(
            model_name='windowsill',
            name='type',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Тип подоконника'),
        ),
        migrations.AlterField(
            model_name='visors',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Развертка'),
        ),
    ]
