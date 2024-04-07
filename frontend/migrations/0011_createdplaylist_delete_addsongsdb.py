# Generated by Django 4.2.4 on 2024-04-07 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0010_addsongsdb_alter_usersdb_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='CreatedPlaylist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UserName', models.CharField(blank=True, max_length=255, null=True)),
                ('PlaylistName', models.CharField(blank=True, max_length=255, null=True)),
                ('Image', models.ImageField(blank=True, default='myplaylist', null=True, upload_to='myplaylist')),
            ],
        ),
        migrations.DeleteModel(
            name='AddsongsDb',
        ),
    ]