# Generated by Django 5.0.3 on 2024-03-25 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('role', models.CharField(max_length=255)),
                ('registration_date', models.DateField()),
                ('last_login_date', models.DateField()),
            ],
        ),
    ]
