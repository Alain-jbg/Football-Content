# Generated by Django 5.0.4 on 2024-04-23 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LeagueStanding',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.IntegerField()),
                ('team', models.CharField(max_length=100)),
                ('matches_played', models.IntegerField()),
                ('wins', models.IntegerField()),
                ('draws', models.IntegerField()),
                ('losses', models.IntegerField()),
                ('goals_for', models.IntegerField()),
                ('goals_against', models.IntegerField()),
                ('goal_difference', models.IntegerField()),
                ('points', models.IntegerField()),
            ],
        ),
    ]
