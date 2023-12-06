from django.db import models
from django import forms
from django.contrib.auth.models import User


# Create your models here.

# class Box(models.Model):
    # value = models.CharField(max_length=255)

class Performance(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)


class Score(models.Model):
    player_name = models.CharField(max_length=100)
    score_value = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)
