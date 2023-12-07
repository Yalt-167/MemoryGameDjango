from django.shortcuts import render, redirect
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
    	
    return render(request,'SignUp.html', {})

# Login
def login_user(request):
    
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
        return ConnectionPage(request)


def HomePage(request):
    return render(request, "home.html")

def HomePageFromElseWhere(request):
    return render(request, "../home.html")

def AboutPage(request):
    return render(request, "about.html")
def ContactPage(request):
    return render(request, "Contact.html")
def LeaderboardPage(request):
    top_performances = Performance.objects.order_by('-score')[:10]
    print(top_performances)
    return render(request, 'leaderboard.html', {'top_performances': top_performances})

# second part are the ones of the far right of our nav bar

def InscriptionPage(request):
    return render(request, "SignUp.html")

def ConnectionPage(request):
    return render(request, "Login.html")