# Generated by Django 3.0.8 on 2021-01-28 15:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restau', '0002_auto_20210128_2018'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='thumbnail',
        ),
    ]
