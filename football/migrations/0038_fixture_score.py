# Generated by Django 5.0.6 on 2024-07-10 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('football', '0037_remove_result_scorer_result_score_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='fixture',
            name='score',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]