from django.db import models

class UsersDb(models.Model):
    Name=models.CharField(null=True, blank=True, max_length=255)
    Email=models.EmailField(null=True, blank=True)
    Username=models.CharField(null=True, blank=True, max_length=255)
    Password=models.CharField(null=True, blank=True, max_length=255)
    Mob_No=models.CharField(null=True, blank=True, max_length=255)
    Profile=models.ImageField(upload_to='profile', null=True, blank=True)