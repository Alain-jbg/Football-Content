# Generated by Django 5.0.6 on 2024-07-09 15:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('football', '0033_competition_teammatch_remove_fixturematch_opponent_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fixturematch',
            name='competition',
            field=models.CharField(max_length=100),
        ),
        migrations.DeleteModel(
            name='TeamMatch',
        ),
        migrations.RemoveField(
            model_name='resultmatch',
            name='details',
        ),
        migrations.RemoveField(
            model_name='resultmatch',
            name='score_away',
        ),
        migrations.RemoveField(
            model_name='resultmatch',
            name='score_home',
        ),
        migrations.AddField(
            model_name='fixturematch',
            name='opponent',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='fixturematch',
            name='team',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='football.team'),
        ),
        migrations.AddField(
            model_name='resultmatch',
            name='goal_details_away',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='resultmatch',
            name='goal_details_home',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='resultmatch',
            name='team_a_score',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='resultmatch',
            name='team_b_score',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='fixturematch',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='fixturematch',
            name='team_away',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='away_fixtures', to='football.club'),
        ),
        migrations.AlterField(
            model_name='fixturematch',
            name='team_home',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='home_fixtures', to='football.club'),
        ),
        migrations.AlterField(
            model_name='resultmatch',
            name='fixture',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='football.fixture'),
        ),
        migrations.DeleteModel(
            name='Competition',
        ),
    ]