# Generated by Django 5.1 on 2024-08-27 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('heros', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hero',
            name='logo',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='hero',
            name='site_desc',
            field=models.TextField(),
        ),
    ]
