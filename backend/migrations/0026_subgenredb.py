# Generated by Django 4.2.4 on 2024-03-19 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0025_rename_genre_img_file_combineddb_com_img_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubGenreDb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Sub_Genre_Name', models.CharField(blank=True, max_length=255, null=True)),
                ('Res_Sub_Genre', models.CharField(blank=True, max_length=255, null=True)),
                ('Sub_Genre_Sbtl', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]
