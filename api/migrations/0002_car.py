# Generated by Django 5.0.3 on 2024-03-19 20:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='car_images/')),
                ('passengers', models.IntegerField()),
                ('doors', models.IntegerField()),
                ('has_air_conditioning', models.BooleanField()),
                ('has_power_locks', models.BooleanField()),
                ('has_power_windows', models.BooleanField()),
                ('fuel_type', models.CharField(max_length=50)),
                ('is_manual', models.BooleanField()),
                ('horsepower', models.IntegerField()),
                ('top_speed', models.IntegerField()),
                ('acceleration_0_100', models.DecimalField(decimal_places=2, max_digits=4)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.brand')),
            ],
        ),
    ]