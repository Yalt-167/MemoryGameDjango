from django.shortcuts import render, HttpResponse
# from .models import Users
# Create your views here.

def Home(request):
    return render(request, "home.html")

# def DisplayUsers(request):
#     items = Users.objects.all()
#     return render(request, "DisplayUsers.html", {"users": items})




from django.shortcuts import render
from .models import Box

def memory_game(request):
    boxes = Box.objects.all()
    return render(request, 'game:memory_game.html',{'boxes':boxes})



