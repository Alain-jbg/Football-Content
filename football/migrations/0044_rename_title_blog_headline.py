# Generated by Django 5.0.4 on 2024-07-24 08:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('football', '0043_rename_title_highlight_headline'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='title',
            new_name='headline',
        ),
    ]
