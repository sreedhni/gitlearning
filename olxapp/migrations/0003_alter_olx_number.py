# Generated by Django 4.2.5 on 2023-09-27 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('olxapp', '0002_olx_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='olx',
            name='number',
            field=models.CharField(max_length=15),
        ),
    ]
