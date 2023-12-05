from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Performance
from django.views import View
# from .models import Box
# from .models import Users
# Create your views here.
# ===============================================================================================
# Verifying the user's login info
def login_user(request):
    if request.method == "POST":
        # Data in the database
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)
        mail = request.POST.get("mail", None)
        user = authenticate(request, username=username, password=password, mail=mail)

    # If the data is same in the database and in the connexion page redirecting toward  the next page
        if user is not None:
            login(request,user)
            return redirect("Home")
            # redirect vers Memory.html
        else:
            return redirect("connexion.html")

    return render(request, 'connexion.html', {})
# ===============================================================================================
class Index(View):
    templatee = "index.html"

    def get (self,request):
        return render(request,self.template)
    
class Login(View):
    template = 'Login.html'

    def get(self,request):
        return render(request,self.template)
    



# ==============================================================================================
# functions that allow for the site to work, they allow the display of the html 
# first part are the ones of the far left of our nav bar
# ==============================================

def Home(request):
    return render(request, "home.html")
def about(request):
    return render(request, "about.html")
def contact(request):
    return render(request, "contact.html")
def leaderboard(request):
    top_performances = Performance.objects.order_by('-score')[:10]
    return render(request, 'leaderboard.html', {'top_performances': top_performances})
# ==============================================
# ===============================================================================================


# ===============================================================================================
# second part are the ones of the far right of our nav bar
# ==============================================

def inscription(request):
    return render(request, "inscription.html")
def connexion(request):
    return render(request, "connexion.html")

# ==============================================
# ===============================================================================================



# def DisplayUsers(request):
#     items = Users.objects.all()
#     return render(request, "DisplayUsers.html", {"users": items})






# def memory_game(request):
#     boxes = Box.objects.all()
#     return render(request, 'game:memory_game.html',{'boxes':boxes})




