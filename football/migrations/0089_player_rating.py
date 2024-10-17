# Generated by Django 5.0.1 on 2024-09-16 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('football', '0088_player_position'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='rating',
            field=models.CharField(blank=True, choices=[('⭐', '1 Star'), ('⭐⭐', '2 Stars'), ('⭐⭐⭐', '3 Stars'), ('⭐⭐⭐⭐', '4 Stars'), ('⭐⭐⭐⭐⭐', '5 Stars')], help_text='Emoji rating (e.g., ⭐⭐⭐⭐, ⭐⭐⭐⭐⭐)', max_length=6, null=True),
        ),
    ]