# Generated by Django 5.0.1 on 2024-08-20 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('football', '0076_fixture_remove_fixtureresult_club_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fixtureresult',
            name='score',
            field=models.CharField(default=0, max_length=20),
        ),
    ]
