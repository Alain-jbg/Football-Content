# Generated by Django 5.0.4 on 2024-07-30 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('football', '0055_alter_blogpost_author_image_alter_blogpost_day_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='day',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
