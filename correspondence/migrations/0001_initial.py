# Generated by Django 4.1.2 on 2022-12-19 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IncomingMail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255)),
                ('preview', models.FileField(upload_to='IncomingMail/')),
            ],
            options={
                'verbose_name': 'Входящая корреспонденция',
                'verbose_name_plural': 'Входящая корреспонденция',
            },
        ),
        migrations.CreateModel(
            name='OutgoingMail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255)),
                ('preview', models.FileField(upload_to='OutgoingMail/')),
            ],
            options={
                'verbose_name': 'Исходящая корреспонденция',
                'verbose_name_plural': 'Исходящая корреспонденция',
            },
        ),
    ]