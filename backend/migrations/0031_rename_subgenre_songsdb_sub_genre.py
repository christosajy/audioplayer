# Generated by Django 4.2.4 on 2024-03-19 14:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0030_songsdb_subgenre'),
    ]

    operations = [
        migrations.RenameField(
            model_name='songsdb',
            old_name='SubGenre',
            new_name='Sub_Genre',
        ),
    ]
