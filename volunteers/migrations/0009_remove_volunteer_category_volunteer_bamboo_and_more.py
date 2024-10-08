# Generated by Django 5.1 on 2024-09-02 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('volunteers', '0008_alter_volunteer_signup_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='volunteer',
            name='category',
        ),
        migrations.AddField(
            model_name='volunteer',
            name='bamboo',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='volunteer',
            name='bees',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='volunteer',
            name='construction',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='volunteer',
            name='eggs',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='volunteer',
            name='goats',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='volunteer',
            name='shiitake',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='volunteer',
            name='vegetables',
            field=models.BooleanField(default=False),
        ),
    ]
