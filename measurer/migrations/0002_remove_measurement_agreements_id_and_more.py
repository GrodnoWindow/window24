# Generated by Django 4.1.2 on 2023-01-17 17:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('measurer', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='measurement',
            name='agreements_id',
        ),
        migrations.AddField(
            model_name='measurement',
            name='agreements',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Изображения'),
        ),
        migrations.AddField(
            model_name='measurement',
            name='final_amount',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Окончательная сумма'),
        ),
        migrations.AddField(
            model_name='measurement',
            name='logs',
            field=models.TextField(blank=True, null=True, verbose_name='Логи замера'),
        ),
        migrations.AddField(
            model_name='measurement',
            name='preliminary_amount',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Предварительная сумма'),
        ),
        migrations.AlterField(
            model_name='measurement',
            name='executor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Исполнитель'),
        ),
    ]
