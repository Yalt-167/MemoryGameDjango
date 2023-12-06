from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from django.contrib import messages
from .models import Performance
from django.views import View
# from .models import Box
# from .models import Users
# Verifying the user's login info

class Index(View):
    template = "index.html"

    def get (self,request):
        return render(request,self.template)
    
class Login(View):
    template = 'Login.html'
    def get(self,request):
        return render(request,self.template)

# functions that allow for the site to work, they allow the display of the html 
# first part are the ones of the far left of our nav bar

def sign_up(request):

    if request.method == "POST":

        username = request.POST["username"]
        password = request.POST["password"]
        email = request.POST["email"]

        user = User.objects.create_user(request,username = username ,email = email , password = password)
        user.save()

    return redirect(request, 'home.html')

def login_user(request):
    if request.method == "POST":
        # Checking the data in the database
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)

        user = authenticate(request, username=username, password=password)

    # If the data is same in the database and in the connexion page redirecting toward  the next page
        if user is not None:
            login(request,user)
            return redirect("../about/")
            # redirect vers Memory.html
        else:
            messages.success(request, ("Identifiant ou mot de passe incorrect"))
            return redirect("contact")
    else:
        return render(request, 'Login.html', {})


def Home(request):
    return render(request, "home.html")
def about(request):
    return render(request, "about.html")
def contact(request):
    return render(request, "contact.html")
def leaderboard(request):
    top_performances = Performance.objects.order_by('-score')[:10]
    return render(request, 'leaderboard.html', {'top_performances': top_performances})

# second part are the ones of the far right of our nav bar

def inscription(request):
    return render(request, "inscription.html")

def connexion(request):
    return render(request, "connexion.html")

# def DisplayUsers(request):
#     items = Users.objects.all()
#     return render(request, "DisplayUsers.html", {"users": items})

# def memory_game(request):
#     boxes = Box.objects.all()
#     return render(request, 'game:memory_game.html',{'boxes's:boxes})