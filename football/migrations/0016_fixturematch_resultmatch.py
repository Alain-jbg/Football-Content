# Generated by Django 5.0.6 on 2024-06-05 06:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('football', '0015_remove_fixture_away_score_remove_fixture_away_team_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='FixtureMatch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('competition', models.CharField(max_length=100)),
                ('opponent', models.CharField(max_length=100)),
                ('venue', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ResultMatch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_a_score', models.IntegerField()),
                ('team_b_score', models.IntegerField()),
                ('fixture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='football.fixture')),
            ],
        ),
    ]
