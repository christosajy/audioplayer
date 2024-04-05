# Generated by Django 4.2.4 on 2024-04-05 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0009_alter_usersdb_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddsongsDb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UserName', models.CharField(blank=True, max_length=255, null=True)),
                ('PlaylistName', models.CharField(blank=True, max_length=255, null=True)),
                ('SongName', models.CharField(blank=True, max_length=255, null=True)),
                ('ArtistName', models.CharField(blank=True, max_length=255, null=True)),
                ('Image', models.ImageField(blank=True, default='myplaylist', null=True, upload_to='myplaylist')),
            ],
        ),
        migrations.AlterField(
            model_name='usersdb',
            name='Profile',
            field=models.ImageField(blank=True, default='profile', null=True, upload_to='profile'),
        ),
    ]
