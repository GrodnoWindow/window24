# Generated by Django 4.1.2 on 2023-01-21 10:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('constructor', '0004_sealbasic_typelamination_typelamination2_and_more'),
        ('calculation', '0003_alter_constructor_gorbylki_alter_constructor_handles_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='constructor',
            name='is_active',
        ),
        migrations.AlterField(
            model_name='constructor',
            name='door',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='constructor.typelamination', verbose_name='Двери'),
        ),
    ]
