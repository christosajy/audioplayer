from django.db import models

class LanguageDb(models.Model):
    Lang_Name = models.CharField(max_length=255, null=True, blank=True)
    Lang_Sbtl = models.CharField(max_length=255, null=True, blank=True)
    Lang_Img = models.ImageField(upload_to='language', null=True, blank=True)

class GenreDb(models.Model):
    LangName = models.CharField(max_length=255, null=True, blank=True)
    GenreName = models.CharField(max_length=255, null=True, blank=True)
    GenreImg = models.ImageField(upload_to='genre', null=True, blank=True)

class SubGenreDb(models.Model):
    GenreName = models.CharField(max_length=255, null=True, blank=True)
    SubName = models.CharField(max_length=255, null=True, blank=True)
    SubImg = models.ImageField(upload_to='genre', null=True, blank=True)

class SongsDb(models.Model):
    No = models.IntegerField(null=True, blank=True)
    Name = models.CharField(max_length=255, null=True, blank=True)
    Language = models.CharField(max_length=255, null=True, blank=True)
    Genre = models.CharField(max_length=255, null=True, blank=True)
    Type = models.CharField(max_length=255, null=True, blank=True)
    Year = models.CharField(max_length=255, null=True, blank=True)
    Artist = models.CharField(max_length=255, null=True, blank=True)
    Film = models.CharField(max_length=255, null=True, blank=True)
    Audio = models.FileField(upload_to='songs', null=True, blank=True)
    Image = models.ImageField(upload_to='cover', null=True, blank=True)
    Extra = models.TextField(null=True, blank=True)

