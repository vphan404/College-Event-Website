# Generated by Django 2.2.7 on 2019-11-20 16:29

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Rso', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rso',
            name='user',
        ),
        migrations.AddField(
            model_name='rso',
            name='members',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
