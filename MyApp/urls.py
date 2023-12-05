from django.urls import path
from .views import Home
from .views import leaderboard
from .views import inscription
from .views import connexion
from .views import about
from .views import contact


urlpatterns = [
    path("", Home, name="Home"),
    # path("", views.DisplayUsers, name="DisplayUsers"),
    path("leaderboard/", leaderboard, name="leaderboard"),
    path("inscription/",inscription, name ="inscription"),
    path("connexion/",connexion, name ="connexion"),
    path("about/",about, name ="about"),
    path("contact/",contact, name ="contact"),
    path("header/",lambda x : x, name ="header"),
]


