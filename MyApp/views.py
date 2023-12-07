from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Score
from django.views import View
from django.shortcuts import render, HttpResponse, redirect
import random as rdm
from .models import User   
from django.views import View
from .Card import Card
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Score

# functions that allow for the site to work, they allow the display of the html 
# first part are the ones of the far left of our nav bar

def SignUp(request):
    print("Blablabla")

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
            return HomePage(request)
            # redirect vers Memory.html
        else:
            messages.success(request, ("Identifiant ou mot de passe incorrect"))
            return ContactPage(request)
    else:
        return LoginPage(request)

def Logout(request):
    print("signout was called")
    if request.user.is_authenticated:
        logout(request)
        print("got through signout")
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
    top_performances = Score.objects.order_by("-score_value")[:10]
    return render(request, "Leaderboards.html", {"top_performances": top_performances})


# Basically what handles the beginining (setup) and end (Results) of the game
@login_required
def MemoryGame(request):
    # list composed of cards with the name meme0 through meme7 with 2 copies fo each
    cards = [Card(f"meme{i}") for i in range(8)] + [Card(f"meme{i}") for i in range(8)]
    # (+) instead of (*2) in order to avoid making copies (meme0 would refer to both card with that label at once -> modifying one would modify the other)
    rdm.shuffle(cards)
    return render(request, "Memory.html", {f"cards": list(enumerate(cards))})

def ParseGameResults(request):
  
    print("Total:", end=" ")
    points: float = request.POST.get("totalPoints", None)
    print(points)

    return HomePage(request)