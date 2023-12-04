from django.db import models

# Creating the Database tabs

class Users(models.Model):
    # Auto incremantation
    # userId = models.AutoField(primary_key = True)

    # User Info
    userEmail = models.CharField(max_length = 100, default = "")
    userName = models.CharField(max_length = 150, default = "")
    userPassword = models.CharField(max_length = 255, default = "")
    userPrivacy = models.BooleanField(default = True) # wether his history is public (True) or only visible to friends (False)


class UserScore(models.Model):
    # Foreign Key
    userId = models.ForeignKey(Users, on_delete = models.CASCADE, default = "")
    # userTime = models. Fonction permettant de connaitre le temps de l'utilisateur
    userScore = models.IntegerField(default = "")
