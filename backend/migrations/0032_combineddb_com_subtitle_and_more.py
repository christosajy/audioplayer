# Generated by Django 4.2.4 on 2024-03-22 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0031_rename_subgenre_songsdb_sub_genre'),
    ]

    operations = [
        migrations.AddField(
            model_name='combineddb',
            name='Com_Subtitle',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='subcombineddb',
            name='Sub_Com_Subtitle',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]