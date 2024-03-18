# Generated by Django 5.0.2 on 2024-03-17 22:01

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_merge_20240312_2019'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='followers',
            field=models.ManyToManyField(blank=True, default=[], related_name='following_users', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='customuser',
            name='followings',
            field=models.ManyToManyField(blank=True, default=[], related_name='follower_users', to=settings.AUTH_USER_MODEL),
        ),
    ]
