# Generated by Django 5.0.1 on 2024-10-11 11:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('football', '0093_delete_feedback'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Match',
            new_name='Matchday',
        ),
    ]
