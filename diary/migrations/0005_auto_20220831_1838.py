# Generated by Django 3.2 on 2022-08-31 15:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('client', '0001_initial'),
        ('diary', '0004_auto_20220831_1833'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='author',
            field=models.CharField(max_length=255, verbose_name='Автор'),
        ),
        migrations.AlterField(
            model_name='task',
            name='client',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='client.client', verbose_name='Клиент'),
        ),
        migrations.AlterField(
            model_name='task',
            name='content',
            field=models.CharField(max_length=255, verbose_name='Контент'),
        ),
        migrations.AlterField(
            model_name='task',
            name='executor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Исполнитель'),
        ),
        migrations.AlterField(
            model_name='task',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Активна'),
        ),
        migrations.AlterField(
            model_name='task',
            name='overdue',
            field=models.BooleanField(default=False, verbose_name='Просрочена'),
        ),
        migrations.AlterField(
            model_name='task',
            name='time_create',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Время создания'),
        ),
        migrations.AlterField(
            model_name='task',
            name='time_deadline',
            field=models.DateTimeField(verbose_name='Срок задачи'),
        ),
        migrations.AlterField(
            model_name='task',
            name='time_update',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Время обновления'),
        ),
        migrations.AlterField(
            model_name='task',
            name='type_task_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='diary.typetask', verbose_name='Тип задачи'),
        ),
    ]