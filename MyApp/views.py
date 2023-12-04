from django.shortcuts import render, HttpResponse
from .models import Performance
# from .models import Box
# from .models import Users
# Create your views here.
# ===============================================================================================


# ===============================================================================================




# ===============================================================================================
# functions that allow for the site to work, they allow the display of the html 
# first part are the ones of the far left of our nav bar
# ==============================================

def Home(request):
    return render(request, "home.phtml")
def about(request):
    return render(request, "about.phtml")
def contact(request):
    return render(request, "contact.phtml")
def leaderboard(request):
    top_performances = Performance.objects.order_by('-score')[:10]
    return render(request, 'leaderboard.phtml', {'top_performances': top_performances})
# ==============================================
# ===============================================================================================


# ===============================================================================================
# second part are the ones of the far right of our nav bar
# ==============================================

def inscription(request):
    return render(request, "inscription.phtml")
def connexion(request):
    return render(request, "connexion.phtml")

# ==============================================
# ===============================================================================================



# def DisplayUsers(request):
#     items = Users.objects.all()
#     return render(request, "DisplayUsers.html", {"users": items})






# def memory_game(request):
#     boxes = Box.objects.all()
#     return render(request, 'game:memory_game.html',{'boxes':boxes})




