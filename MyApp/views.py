
from django.shortcuts import render, HttpResponse, redirect
import random as rdm
from .models import Performance
from django.views import View

# Create your views here.
# file where the differents pages are created
# a render is made from a .html file known as template (allow us to embed python code in it)
# -> the render enables us to pass arguments in the .html (as a JSON) making more dynamic pages possible


class Card:
    def __init__(self, name: str) -> None:
        self.name: str = name

# ===============================================================================================


# ===============================================================================================
class Index(View):
    template = "index.html"

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

    return render(request, "home.html")