from django.contrib import admin
from MyApp import views

from django.urls import path
# from .views import Home
# from .views import leaderboard
# from .views import inscription
# from .views import connexion
# from .views import about
# from .views import contact
# from .views import login


urlpatterns = [
    path("", views.HomePage, name="Home"),
    path("../", views.HomePageFromElseWhere, name="HomeFromElsewhere"),
    # path("", views.DisplayUsers, name="DisplayUsers"),
    path("Memory/", views.MemoryGame, name="Memory"),
    path("Leaderboards/", views.LeaderboardPage, name="Leaderboards"),
    path("About/",views.AboutPage, name ="About"),
    path("Contact/",views.ContactPage, name ="Contact"),
    path("Header/",lambda x : x, name ="Header"),
    path('Login/', views.Login, name='Login'),
    path('SignUp/', views.SignUp, name='SignUp'),
    path('Logout/', views.Logout, name='Logout'),
]



