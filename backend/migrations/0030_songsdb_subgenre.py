# Generated by Django 4.2.4 on 2024-03-19 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0029_rename_sub_com_subgenre_subcombineddb_sub_com_res_subgenre_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='songsdb',
            name='SubGenre',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
