from django.urls import path
from . import views

urlpatterns = [
    path("", views.Home, name="Home"),
    path("DisplayUsers", views.DisplayUsers, name="DisplayUsers"),
    path('', MemoryGameView.as_view(), name='memory_game'),
    path('flip_card/<int:card_id>/', flip_card, name='flip_card')
]