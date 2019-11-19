# Generated by Django 2.1.7 on 2019-11-19 13:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Events', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='eventDatetime',
            new_name='datetime',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='eventDescription',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='eventId',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='eventName',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='event',
            name='eventDate',
        ),
        migrations.RemoveField(
            model_name='event',
            name='eventTime',
        ),
    ]
