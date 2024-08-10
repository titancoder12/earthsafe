# Generated by Django 4.1 on 2024-08-10 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Earthquake',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('magnitude', models.IntegerField()),
                ('place', models.CharField(max_length=64)),
                ('time', models.TimeField()),
                ('tsunami', models.IntegerField()),
            ],
        ),
    ]
