# Generated by Django 5.1 on 2024-09-06 01:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medias', '0010_alter_media_image_b64'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='media',
            name='image_b64',
        ),
    ]
