# Generated by Django 4.2.4 on 2024-04-03 10:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0034_remove_combineddb_com_subtitle_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CombinedDb',
        ),
        migrations.DeleteModel(
            name='SubCombinedDb',
        ),
        migrations.RenameField(
            model_name='genredb',
            old_name='Genre_Name',
            new_name='Genre',
        ),
        migrations.RenameField(
            model_name='languagedb',
            old_name='Language_Image',
            new_name='Lang_Img',
        ),
        migrations.RenameField(
            model_name='languagedb',
            old_name='Language_Subtitle',
            new_name='Lang_Name',
        ),
        migrations.RenameField(
            model_name='languagedb',
            old_name='Language_Name',
            new_name='Lang_Sbtl',
        ),
        migrations.RenameField(
            model_name='subgenredb',
            old_name='Sub_Genre_Name',
            new_name='SubGenre_Name',
        ),
    ]