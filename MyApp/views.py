from django.shortcuts import render, HttpResponse
from .models import Users
# Create your views here.

def Home(request):
    return render(request, "home.html")

def DisplayUsers(request):
    items = Users.objects.all()
    return render(request, "DisplayUsers.html", {"users": items})