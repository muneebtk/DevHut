# Generated by Django 4.1 on 2022-09-23 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_likes_follower'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='likes',
            field=models.IntegerField(default=0, max_length=50),
        ),
    ]
