# Generated by Django 4.2.4 on 2024-03-19 11:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0027_subcombineddb'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subcombineddb',
            old_name='Sub_Com_Language',
            new_name='Sub_Com_SubGenre',
        ),
    ]