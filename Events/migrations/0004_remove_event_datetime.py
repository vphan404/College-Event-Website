# Generated by Django 2.1.7 on 2019-11-20 02:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Events', '0003_auto_20191119_2058'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='datetime',
        ),
    ]
