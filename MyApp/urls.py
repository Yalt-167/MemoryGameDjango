from django.contrib import admin
from MyApp import views
from django.urls import path
from .views import Home
from .views import leaderboard
from .views import inscription
from .views import connexion
from .views import about
from .views import contact
from .views import Login


urlpatterns = [
    path("", Home, name="Home"),
    # path("", views.DisplayUsers, name="DisplayUsers"),
    path("leaderboard/", leaderboard, name="leaderboard"),
    path("inscription/",inscription, name ="inscription"),
    path("connexion/",connexion, name ="connexion"),
    path("about/",about, name ="about"),
    path("contact/",contact, name ="contact"),
    path("header/",lambda x : x, name ="header"),
    path('', views.Index.as_view(), name='index'),
    path('login/', views.Login.as_view(), name='Login'),
]


