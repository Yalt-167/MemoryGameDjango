
from django.shortcuts import render, HttpResponse, redirect
import random as rdm
from .models import Performance, User   
from django.views import View
from .Card import Card
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
# file where the differents pages are created
# a render is made from a .html file known as template (allow us to embed python code in it)
# -> the render enables us to pass arguments in the .html (as a JSON) making more dynamic pages possible




# ==============================================================================================
# functions that allow for the site to work, they allow the display of the html 
# first part are the ones of the far left of our nav bar
# ==============================================

def HomePage(request):
    return render(request, "home.html")

def AboutPage(request):
    return render(request, "about.html")

def ContactPage(request):
    return render(request, "contact.html")

def LeaderboardPage(request):
    top_performances = Performance.objects.order_by("-score")[:10]
    return render(request, "leaderboard.html", {"top_performances": top_performances})

# ===============================================================================================
# second part are the ones of the far right of our nav bar
# ==============================================

def SignUpPage(request):
    return render(request, "SignUp.html")

def LoginPage(request):
    return render(request, "Login.html")

# ===============================================================================================

def SignUp(request):
    print("signup was called")
    if request.method == "POST":

        username = request.POST.get("username", None)
        email = request.POST.get("email", None)
        password = request.POST.get("password", None)

        if username is not None and email is not None and password is not None:

            user = User.objects.create_user(
                username=username,
                email=email,
                password=password
            )

            user.save()

            login(request, user)
            print("got through signup")

    return HomePage(request)

def LoginFunction(request):
    print("login was called")
    if request.method == "POST":

        user = authenticate(
            request,
            username=request.POST.get("username", None),
            password=request.POST.get("password", None)
            )

        if user is not None:
            login(request, user)
            print("got through login")
            return HomePage(request)
        else:
            messages.success(request, ("Identifiant ou mot de passe incorrect"))
            return LoginPage(request)
    else:
        return render(request, "Login.html", {})


def SignOut(request):
    print("signout was called") # perhaps the print doesn t take effect in that specific context
    if request.user.is_authenticated:
        logout(request, request.user)
        print("got through signout")
    return HomePage(request)


# ===============================================================================================

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