# Generated by Django 5.0.1 on 2024-09-16 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('football', '0090_remove_player_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='red_cards',
        ),
        migrations.RemoveField(
            model_name='player',
            name='yellow_cards',
        ),
        migrations.AddField(
            model_name='player',
            name='red_card_image',
            field=models.ImageField(blank=True, null=True, upload_to='red_cards/'),
        ),
        migrations.AddField(
            model_name='player',
            name='yellow_card_image',
            field=models.ImageField(blank=True, null=True, upload_to='yellow_cards/'),
        ),
    ]
