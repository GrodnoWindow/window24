# Generated by Django 3.2 on 2022-08-31 15:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0001_initial'),
        ('diary', '0002_alter_task_executor'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='client',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='client.client'),
        ),
    ]
