# Generated by Django 5.0.3 on 2024-03-14 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0017_remove_genredb_genre_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='songsdb',
            name='Artists',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='songsdb',
            name='Year',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
