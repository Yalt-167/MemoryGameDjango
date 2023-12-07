from django.db import models
from django.contrib.auth.models import User


# Create your models here

class UserHistory(models.Model):
    date = models.DateTimeField(auto_now_add=True, primary_key=True)
    score = models.IntegerField(default=0)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    history = UserHistory()
    bio = models.TextField(blank=True)
    # profilePicture = models.ImageField(upload_to='profile_pics/', blank=True) // if we get to bonus parts

class Score(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score_value = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)
  
