# Generated by Django 3.0.8 on 2021-01-29 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restau', '0004_auto_20210129_1738'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='type',
            field=models.CharField(max_length=20),
        ),
    ]
