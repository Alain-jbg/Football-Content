# Generated by Django 5.0.4 on 2024-07-30 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('football', '0057_remove_blogpost_author_image_remove_blogpost_image_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpost',
            name='photo',
        ),
        migrations.AddField(
            model_name='blogpost',
            name='author_image',
            field=models.ImageField(blank=True, null=True, upload_to='author_images/'),
        ),
    ]
