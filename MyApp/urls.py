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
    path("Leaderboards/", views.LeaderboardPage, name="Leaderboards"),
    path("",views.HomePage, name ="Home"),
    path("Contact/",views.ContactPage, name ="Contact"),
    path("About/",views.AboutPage, name ="About"),
    path("Header/",lambda x : x, name ="Header"),
    # path('', views.Index.as_view(), name='index'),
    path('SignUp/', views.SignUp, name='SignUp'),
    path('Login/', views.Login, name='Login'),
    path('LogOut/', views.Logout, name='Logout'),
    path('Memory/', views.MemoryGame, name="MemoryGame"),
    path('../', views.ParseGameResults, name="ParseGameResults"),
    path('Us', views.UsPage, name="Us"),
]



