from django.db import models

class UsersDb(models.Model):
    Name=models.CharField(null=True, blank=True, max_length=255)
    Email=models.EmailField(null=True, blank=True)
    Username=models.CharField(null=True, blank=True, max_length=255)
    Password=models.CharField(null=True, blank=True, max_length=255)
    Mob_No=models.CharField(null=True, blank=True, max_length=255)
    Profile=models.ImageField(upload_to='profile', null=True, blank=True, default='profile')

class PlaylistsDb(models.Model):
    SongName=models.CharField(null=True, blank=True, max_length=255)
    UserName=models.CharField(null=True, blank=True, max_length=255)
    ArtistName=models.CharField(null=True, blank=True, max_length=255)

class AddsongsDb(models.Model):
    UserName=models.CharField(null=True, blank=True, max_length=255)
    PlaylistName=models.CharField(null=True, blank=True, max_length=255)
    SongName=models.CharField(null=True, blank=True, max_length=255)
    ArtistName=models.CharField(null=True, blank=True, max_length=255)
    Image=models.ImageField(upload_to='myplaylist', null=True, blank=True, default='myplaylist')
