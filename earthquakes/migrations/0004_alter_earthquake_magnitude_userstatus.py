# Generated by Django 4.1 on 2024-08-10 20:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('earthquakes', '0003_alter_earthquake_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='earthquake',
            name='magnitude',
            field=models.FloatField(),
        ),
        migrations.CreateModel(
            name='UserStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=10)),
                ('earthquake_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='earthquakes.earthquake')),
                ('person_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
