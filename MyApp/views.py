from django.shortcuts import render, HttpResponse, redirect
import random as rdm
# Create your views here.
# file where the differents pages are created
# a render is made from a .html file known as template (allow us to embed python code in it)
# -> the render enables us to pass arguments in the .html (as a JSON) making more dynamic pages possible
class Card:
    def __init__(self, name: str) -> None:
        self.name: str = name

def Home(request):
    return render(request, "home.html")

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