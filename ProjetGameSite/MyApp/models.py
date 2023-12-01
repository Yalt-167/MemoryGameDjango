from django.db import models

# Create your models here.

class Users(models.Model):
    userEmail = models.CharField(max_length=255)
    userName = models.CharField(max_length=255)
    userPrivacy = models.BooleanField() # wether his history is public (True) or only visible to friends (False)