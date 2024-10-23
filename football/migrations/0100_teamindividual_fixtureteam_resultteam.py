# Generated by Django 5.0.1 on 2024-10-18 12:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('football', '0099_alter_feedback_rating'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeamIndividual',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='team_logos/')),
            ],
        ),
        migrations.CreateModel(
            name='FixtureTeam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('competition', models.CharField(max_length=100)),
                ('date', models.DateTimeField()),
                ('opponent', models.CharField(max_length=100)),
                ('venue', models.CharField(max_length=100)),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='football.team')),
            ],
        ),
        migrations.CreateModel(
            name='ResultTeam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('home_score', models.IntegerField()),
                ('away_score', models.IntegerField()),
                ('home_goal_scorers', models.TextField()),
                ('away_goal_scorers', models.TextField()),
                ('fixture_team', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='football.fixtureteam')),
            ],
        ),
    ]