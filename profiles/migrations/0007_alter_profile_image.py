# Generated by Django 5.1.5 on 2025-03-10 21:32

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0006_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=cloudinary.models.CloudinaryField(default='default_profile_girwrs.jpg', max_length=255, verbose_name='images'),
        ),
    ]
