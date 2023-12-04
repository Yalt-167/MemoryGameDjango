from django.shortcuts import render, HttpResponse
from .models import Performance
# from .models import Box
# from .models import Users
# Create your views here.

def Home(request):
    return render(request, "home.html")

def leaderboard(request):
    top_performances = Performance.objects.order_by('-score')[:10]
    return render(request, 'leaderboard.html', {'top_performances': top_performances})

def inscription(request):
    return render(request, "inscription.html")


# def DisplayUsers(request):
#     items = Users.objects.all()
#     return render(request, "DisplayUsers.html", {"users": items})






# def memory_game(request):
#     boxes = Box.objects.all()
#     return render(request, 'game:memory_game.html',{'boxes':boxes})




