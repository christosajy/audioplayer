# Generated by Django 5.0.3 on 2024-03-07 14:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0006_rename_song_name_audiodb_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='audiodb',
            name='Artist',
        ),
    ]
