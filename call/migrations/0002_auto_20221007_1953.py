# Generated by Django 3.2 on 2022-10-07 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('call', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Call_Okna',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_call', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='call',
            name='client_id',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]