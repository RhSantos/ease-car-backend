# Generated by Django 5.0.3 on 2024-03-21 17:28

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_rental'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='rental',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]