# Generated by Django 4.1 on 2022-10-05 10:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0023_likes_liked_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='likes',
            name='liked_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
