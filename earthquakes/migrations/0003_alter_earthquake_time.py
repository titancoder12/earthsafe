# Generated by Django 4.1 on 2024-08-10 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('earthquakes', '0002_earthquake_api_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='earthquake',
            name='time',
            field=models.DateTimeField(),
        ),
    ]
