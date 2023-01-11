# Generated by Django 4.1.2 on 2022-12-19 22:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('call', '0001_initial'),
        ('client', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='CallsTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('call', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='call.call')),
                ('client', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='client.client')),
            ],
        ),
    ]