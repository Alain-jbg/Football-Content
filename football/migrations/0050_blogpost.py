# Generated by Django 5.0.4 on 2024-07-29 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('football', '0049_remove_blog_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=100)),
                ('date_published', models.DateField()),
                ('content', models.TextField()),
            ],
        ),
    ]