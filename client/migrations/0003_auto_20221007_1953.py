# Generated by Django 3.2 on 2022-10-07 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0002_rename_number_client_numbers'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.RenameField(
            model_name='number',
            old_name='number',
            new_name='name',
        ),
        migrations.AddField(
            model_name='client',
            name='addresses',
            field=models.ManyToManyField(blank=True, null=True, to='client.Address'),
        ),
    ]