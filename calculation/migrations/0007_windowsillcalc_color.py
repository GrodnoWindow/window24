# Generated by Django 4.1.2 on 2023-02-20 16:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('constructor', '0006_windowsillcolor_alter_windowsill_color'),
        ('calculation', '0006_alter_internalslopecalc_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='windowsillcalc',
            name='color',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='constructor.windowsillcolor', verbose_name='Установка'),
        ),
    ]