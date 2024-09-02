# Generated by Django 5.1 on 2024-09-02 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bamboo', models.BooleanField(default=False)),
                ('vegetables', models.BooleanField(default=False)),
                ('eggs', models.BooleanField(default=False)),
                ('shiitake', models.BooleanField(default=False)),
                ('bees', models.BooleanField(default=False)),
                ('goats', models.BooleanField(default=False)),
                ('construction', models.BooleanField(default=False)),
            ],
        ),
    ]
