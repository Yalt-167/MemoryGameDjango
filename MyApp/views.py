from django.shortcuts import render, HttpResponse, redirect
from .models import Card
import random as rdm
# Create your views here.
# file where the differents pages are created
# a render is made from a .html file known as template (allow us to embed python code in it)
# -> the render enables us to pass arguments in the .html making dynamic pages possible

def Home(request):
    return render(request, "home.html")

# def flip_card(request, card_id):
#     card = Card.objects.get(pk=card_id)

#     if not card.paired:
#         card.paired = True
#         card.save()

#     return redirect("Memory.html")

def MemoryGame(request):
    cards = SetupCards()
    rdm.shuffle(cards)
    return render(request, "Memory.html", {f"cards": cards})

def SetupCards() -> list[Card]:
    Card.objects.all().delete()
    # makes a list composed of cards with the name meme0 through meme7 with 2 copies fo each
    cards: list[Card] = [Card(f"meme{i}") for i in range(8)] + [Card(f"meme{i}") for i in range(8)]
    # + instead of *2 in order to avoid making copies (meme0 would refer to both card with that label at once -> modifying one would modify the other)
    for card in cards:
        card.save()
    return cards