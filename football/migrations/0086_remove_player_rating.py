# Generated by Django 5.0.1 on 2024-09-16 01:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('football', '0085_remove_staff_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='rating',
        ),
    ]