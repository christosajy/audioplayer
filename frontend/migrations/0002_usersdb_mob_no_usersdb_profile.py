# Generated by Django 4.2.4 on 2024-03-24 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usersdb',
            name='Mob_No',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='usersdb',
            name='Profile',
            field=models.ImageField(blank=True, null=True, upload_to='profile'),
        ),
    ]
