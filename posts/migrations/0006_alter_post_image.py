# Generated by Django 5.1.5 on 2025-01-23 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_alter_post_tags_alter_tag_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, default='../default_post_f3ugv9', upload_to='images/'),
        ),
    ]
