from django.contrib import admin
from MyApp import views
from django.urls import path

from .views import Home, MemoryGame, ParseGameResults
from .views import leaderboard
from .views import inscription
from .views import connexion
from .views import about
from .views import contact
from .views import Login

urlpatterns = [
    path("", Home, name="Home"), # name -> associate a unique name to the path so u can refer to it using the name (in temlpates) or using reverse(name) (in regular python)
    path("Memory/", MemoryGame, name="Memory"),
    path("", ParseGameResults, name="ParseGameResults"),
    path("leaderboard/", leaderboard, name="leaderboard"),
    path("inscription/",inscription, name ="inscription"),
    path("connexion/",connexion, name ="connexion"),
    path("about/",about, name ="about"),
    path("contact/",contact, name ="contact"),
    path("header/",lambda x : x, name ="header"),
    path('', views.Index.as_view(), name='index'),
    path('login/', views.Login.as_view(), name='Login'),
]

