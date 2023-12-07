from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Performance
from django.views import View
from django.shortcuts import render, HttpResponse, redirect
import random as rdm
from .models import Performance, User   
from django.views import View
from .Card import Card
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# from .models import Box
# from .models import Users
# Verifying the user's login info

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
            return redirect("http://127.0.0.1:8000/about/")
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
            return AboutPage(request)
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
    return redirect("http://127.0.0.1:8000/about/")


def HomePage(request):
    return render(request, "Home.html")

def HomePageFromElseWhere(request):
    return render(request, "../Home.html")

# second part are the ones of the far right of our nav bar

def SignUpPage(request):
    return render(request, "SignUp.html")

def LoginPage(request):
    return render(request, "Login.html")


def AboutPage(request):
    return render(request, "About.html")

def ContactPage(request):
    return render(request, "Contact.html")

def LeaderboardPage(request):

    top_performances = list(Performance.objects.order_by("-score"))[:10]
    print(top_performances)
    return render(request, "Leaderboards.html", {"top_performances": top_performances})


# def SignUp(request):
#     print("signup was called")
#     if request.method == "POST":

#         username = request.POST.get("username", None)
#         email = request.POST.get("email", None)
#         password = request.POST.get("password", None)

#         if username is not None and email is not None and password is not None:

#             user = User.objects.create_user(
#                 username=username,
#                 email=email,
#                 password=password
#             )

#             user.save()

#             login(request, user)
#             print("got through signup")

#     return HomePage(request)

# def LoginFunction(request):
#     print("login was called")
#     if request.method == "POST":

#         user = authenticate(
#             request,
#             username=request.POST.get("username", None),
#             password=request.POST.get("password", None)
#             )

#         if user is not None:
#             login(request, user)
#             print("got through login")
#             return HomePage(request)
#         else:
#             messages.success(request, ("Identifiant ou mot de passe incorrect"))
#             return LoginPage(request)
#     else:
#         return render(request, "Login.html", {})


# def SignOut(request):
#     print("signout was called") # perhaps the print doesn t take effect in that specific context
#     if request.user.is_authenticated:
#         logout(request, request.user)
#         print("got through signout")
#     return HomePage(request)


# ===============================================================================================

# Basically what handles the beginining (setup) and end (Results) of the game
@login_required
def MemoryGame(request):
    if not request.user.is_authentificated: return HomePage(request)

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