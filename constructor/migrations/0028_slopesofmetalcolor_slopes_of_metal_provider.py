# Generated by Django 4.1.2 on 2023-09-10 08:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('constructor', '0027_rename_internal_slope_provider_slopesofmetal_slopes_of_metal_provider'),
    ]

    operations = [
        migrations.AddField(
            model_name='slopesofmetalcolor',
            name='slopes_of_metal_provider',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='constructor.slopesofmetalprovider', verbose_name='Поставщик'),
        ),
    ]
