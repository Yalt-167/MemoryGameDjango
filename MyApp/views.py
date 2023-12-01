from django.shortcuts import render, HttpResponse, redirect
from django.views import View
from .models import Card
import random as rdm
# Create your views here.

def Home(request):
    return render(request, "home.html")

def DisplayUsers(request):
    # items = Users.objects.all()
    return render(request, "DisplayUsers.html", {"users": items})


class MemoryGameView(View):
    template_name = 'game/memory_game.html'

    def get(self, request):
        cards = Card.objects.all()

        # Shuffle the cards
        card_list = list(cards)
        random.shuffle(card_list)

        return render(request, self.template_name, {'cards': card_list})


def flip_card(request, card_id):
    card = Card.objects.get(pk=card_id)

    if not card.paired:
        card.paired = True
        card.save()

    return redirect('memory_game')