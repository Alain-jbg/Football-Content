# Generated by Django 5.0.1 on 2024-10-11 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('football', '0096_rename_time_fixtureresult_time_taken'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback_text', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
