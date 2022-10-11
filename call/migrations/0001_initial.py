# Generated by Django 3.2 on 2022-10-04 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Call',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_call', models.CharField(blank=True, max_length=255)),
                ('number', models.CharField(max_length=255)),
                ('datetime', models.DateTimeField(blank=True)),
                ('call_status', models.CharField(blank=True, max_length=255)),
                ('call_type', models.CharField(blank=True, max_length=255)),
                ('name_client', models.CharField(blank=True, max_length=255)),
                ('status', models.CharField(blank=True, max_length=255)),
                ('comment', models.CharField(blank=True, max_length=255)),
                ('manager', models.CharField(blank=True, max_length=255)),
            ],
        ),
    ]