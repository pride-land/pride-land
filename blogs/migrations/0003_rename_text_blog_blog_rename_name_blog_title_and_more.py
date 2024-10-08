import django.db.models.deletion
from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_alter_blog_img_url'),
        ('medias', '0002_alter_media_img_url'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='text',
            new_name='blog',
        ),
        migrations.RenameField(
            model_name='blog',
            old_name='name',
            new_name='title',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='img_url',
        ),
        migrations.AddField(
            model_name='blog',
            name='images',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='medias.media'),
        ),
    ]
