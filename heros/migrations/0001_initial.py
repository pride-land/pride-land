# Generated by Django 5.1 on 2024-08-27 03:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('medias', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_desc', models.TextField(null=True)),
                ('logo', models.TextField(null=True)),
                ('img_url', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='medias.media')),
            ],
        ),
    ]
