# Generated by Django 5.0.3 on 2024-03-19 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_car'),
    ]

    operations = [
        migrations.RenameField(
            model_name='car',
            old_name='is_manual',
            new_name='is_automatic',
        ),
        migrations.AlterField(
            model_name='brand',
            name='image',
            field=models.ImageField(upload_to='brand/'),
        ),
        migrations.AlterField(
            model_name='car',
            name='fuel_type',
            field=models.CharField(choices=[('Gasoline', 'Gasoline'), ('Diesel', 'Diesel'), ('Propane', 'Propane'), ('CNG', 'Cng'), ('Ethanol', 'Ethanol'), ('Bio-diesel', 'Biodiesel')], default='Gasoline', max_length=20),
        ),
        migrations.AlterField(
            model_name='car',
            name='image',
            field=models.ImageField(upload_to='car/'),
        ),
    ]
