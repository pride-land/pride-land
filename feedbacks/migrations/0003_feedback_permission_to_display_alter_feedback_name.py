# Generated by Django 5.1 on 2024-09-12 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedbacks', '0002_feedback_is_accepted'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='permission_to_display',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
