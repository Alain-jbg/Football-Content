# Generated by Django 5.0.4 on 2024-07-30 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('football', '0059_highlight'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='image_url',
        ),
        migrations.RemoveField(
            model_name='blogpost',
            name='author_image',
        ),
        migrations.RemoveField(
            model_name='highlight',
            name='url',
        ),
        migrations.AddField(
            model_name='blog',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='blog_images/'),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='blogpost_images/'),
        ),
    ]
