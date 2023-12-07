from django.contrib import admin
from MyApp import views
from django.urls import path

urlpatterns = [
    path("../", views.HomePage, name="Home"), # name -> associate a unique name to the path so u can refer to it using the name (in temlpates) or using reverse(name) (in regular python)
    path("Memory/", views.MemoryGame, name="Memory"),
    path("", views.ParseGameResults, name="ParseGameResults"),
    path("Leaderboard/", views.LeaderboardPage, name="Leaderboard"),
    path("SignUp/",views.SignUpPage, name ="SignUp"),
    path("About/",views.AboutPage, name ="About"),
    path("Contact/",views.ContactPage, name ="Contact"),
    path('Login/', views.LoginPage, name='Login'),    
    path("../", views.LoginFunction, name='LoginFunction'),
    path("../", views.SignUp, name='SignUpFunction'),
    path("Header/",lambda x : x, name ="Header"),
]