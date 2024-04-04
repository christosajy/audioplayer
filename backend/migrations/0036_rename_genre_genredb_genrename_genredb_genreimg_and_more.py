# Generated by Django 4.2.4 on 2024-04-03 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0035_delete_combineddb_delete_subcombineddb_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='genredb',
            old_name='Genre',
            new_name='GenreName',
        ),
        migrations.AddField(
            model_name='genredb',
            name='GenreImg',
            field=models.ImageField(blank=True, null=True, upload_to='genre'),
        ),
        migrations.AddField(
            model_name='genredb',
            name='LangName',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
