from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Score
from django.views import View
from django.shortcuts import render, HttpResponse, redirect
import random as rdm  
from .Card import Card
import datetime
# functions that define how a site should be rendered based on a template -> .html files that hold logic for further customization

def SignUp(request):

    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
            print("User created successfully")
            return redirect("http://127.0.0.1:8000/About/")
        except Exception as e:
            print(f"Error creating user: {e}")
    	
    return SignUpPage(request)

def Login(request):
    
    if request.method == "POST":
        # Checking the data in the database
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)

        user = authenticate(request, username=username, password=password)

    # If the data is same in the database and in the connexion page redirecting toward  the next page
        if user is not None:
            login(request,user)
            [
                Score(
                    user=request.user,
                    score_value=rdm.randint(0, 100),
                    timestamp=datetime.datetime.now()).save() for _ in range(rdm.randint(3, 10))
                    ]
            return HomePage(request)
            # redirect vers Memory.html
        else:
            messages.error(request, ("Identifiant ou mot de passe incorrect"))
            # messages.success()
            return ContactPage(request)
    else:
        return LoginPage(request)

def Logout(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect("http://127.0.0.1:8000/About/")

def HomePage(request):
    return render(request, "Home.html")
def HomePageFromElseWhere(request):
    return render(request, "../Home.html")
def AboutPage(request):
    return render(request, "About.html")
def ContactPage(request):
    return render(request, "Contact.html")
def UsPage(request):
    return render(request, "Us.html")

# second part are the ones of the far right of our nav bar

def SignUpPage(request):
    return render(request, "SignUp.html")

def LoginPage(request):
    return render(request, "Login.html")

def LeaderboardPage(request):
    return render(request, "Leaderboards.html", {"topScores": Score.objects.order_by("-score_value")[::-1]})


# Basically what handles the beginining (setup) and end (Results) of the game

def SetupCards():
    cards = [Card(f"meme{i}") for i in range(8)] + [Card(f"meme{i}") for i in range(8)]
    # (+) instead of (*2) in order to avoid making copies (meme0 would refer to both card with that label at once -> modifying one would modify the other)
    rdm.shuffle(cards)

    return cards

def MemoryGame(request):
    if not request.user.is_authenticated:
        return LoginPage(request)
    # list composed of cards with the name meme0 through meme7 with 2 copies fo each
    cards = SetupCards()
    return render(request, "Memory.html", {f"cards": list(enumerate(cards))})

def ParseGameResults(request):
    Score(user=request.user, score_value=request.POST.get("totalPoints", None), timestamp=datetime.datetime.now()).save()
    return HomePage(request)