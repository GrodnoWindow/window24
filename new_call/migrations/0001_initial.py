# Generated by Django 4.1.2 on 2023-07-09 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OutgoingCalls',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(blank=True, max_length=255, null=True)),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('number', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
