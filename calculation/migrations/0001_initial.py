# Generated by Django 3.2 on 2022-10-11 20:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('constructor', '0009_delete_windowdiscount'),
    ]

    operations = [
        migrations.CreateModel(
            name='WindowDiscount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discount', models.FloatField(default=0.0, max_length=255)),
                ('fittings_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='constructor.fittings', verbose_name='фурнитура')),
                ('profile_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='constructor.profile', verbose_name='Профиль')),
            ],
            options={
                'verbose_name': 'Скидка на окно',
                'verbose_name_plural': 'Скидки на окна',
            },
        ),
    ]