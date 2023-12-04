from django.db import models

# Create your models here.

# models.py
from django.contrib.auth.models import User

# Creating an user history
class UserHistory(models.Model):
    date = models.DateTimeField(auto_now_add=True, primary_key=True)
    score = models.IntegerField(default=0)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Add additional fields as needed
    history = UserHistory()
    bio = models.TextField(blank=True)
    # profilePicture = models.ImageField(upload_to='profile_pics/', blank=True) // if we get to bonus parts


    
