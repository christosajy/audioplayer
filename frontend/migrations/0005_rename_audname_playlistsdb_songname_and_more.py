# Generated by Django 4.2.4 on 2024-04-01 13:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0004_rename_name_playlistsdb_audname_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='playlistsdb',
            old_name='AudName',
            new_name='SongName',
        ),
        migrations.RenameField(
            model_name='playlistsdb',
            old_name='Username',
            new_name='UserName',
        ),
    ]
