from django.db import models

class LanguageDb(models.Model):
    Language_Name = models.CharField(max_length=255, null=True, blank=True)
    Language_Subtitle = models.CharField(max_length=255, null=True, blank=True)
    Language_Image = models.ImageField(upload_to='language', null=True, blank=True)

class SongsDb(models.Model):
    Srl_Num = models.IntegerField(null=True, blank=True)
    Name = models.CharField(max_length=255, null=True, blank=True)
    Language = models.CharField(max_length=255, null=True, blank=True)
    Genre = models.CharField(max_length=255, null=True, blank=True)
    Sub_Genre = models.CharField(max_length=255, null=True, blank=True)
    Year = models.CharField(max_length=255, null=True, blank=True)
    Artists = models.CharField(max_length=255, null=True, blank=True)
    Album_or_Film = models.CharField(max_length=255, null=True, blank=True)
    Audio_File = models.FileField(upload_to='songs', null=True, blank=True)
    Img_File = models.ImageField(upload_to='cover', null=True, blank=True)

class GenreDb(models.Model):
    Genre_Language = models.CharField(max_length=255, null=True, blank=True)
    Genre_Name = models.CharField(max_length=255, null=True, blank=True)
    Genre_Subtitle = models.CharField(max_length=255, null=True, blank=True)

class SubGenreDb(models.Model):
    Sub_Genre_Name = models.CharField(max_length=255, null=True, blank=True)
    Res_Sub_Genre = models.CharField(max_length=255, null=True, blank=True)
    Sub_Genre_Sbtl = models.CharField(max_length=255, null=True, blank=True)

class CombinedDb(models.Model):
    Com_Language = models.CharField(max_length=255, null=True, blank=True)
    Com_Genre = models.CharField(max_length=255, null=True, blank=True)
    Com_Img_File = models.ImageField(upload_to='combine', null=True, blank=True)

class SubCombinedDb(models.Model):
    Sub_Com_Genre = models.CharField(max_length=255, null=True, blank=True)
    Sub_Com_Res_SubGenre = models.CharField(max_length=255, null=True, blank=True)
    Sub_Com_Img_File = models.ImageField(upload_to='subcomb', null=True, blank=True)