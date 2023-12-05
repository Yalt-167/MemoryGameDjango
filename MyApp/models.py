from django.db import models

# Create your models here.

class Card(models.Model):
    name: str = models.CharField(max_length=255, primary_key=True, default="")