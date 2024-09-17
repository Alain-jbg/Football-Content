# Generated by Django 5.0.1 on 2024-09-13 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('football', '0083_alter_staff_role_alter_staff_staff_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='role',
            field=models.CharField(choices=[('Head Coach', 'Head Coach'), ('Assistant Coach', 'Assistant Coach'), ('Director', 'Diretor'), ('Project Manager', 'Project Manager'), ('Community Engager', 'Community Engager'), ('Backend Developer', 'Backend Developer'), ('Frontend Developer', 'Frontend Developer')], max_length=100),
        ),
    ]
