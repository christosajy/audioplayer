# Generated by Django 5.0.3 on 2024-03-06 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_rename_language_languagedb'),
    ]

    operations = [
        migrations.CreateModel(
            name='SongDb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Song', models.FileField(upload_to='')),
                ('Song_Name', models.CharField(max_length=255)),
            ],
        ),
    ]
