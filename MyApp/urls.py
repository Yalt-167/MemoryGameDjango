from MyApp import views
from django.urls import path


urlpatterns = [
    path("", views.HomePage, name="Home"),
    path("../", views.HomePageFromElseWhere, name="HomeFromElsewhere"),
    # path("", views.DisplayUsers, name="DisplayUsers"),
    path("Leaderboards/", views.LeaderboardPage, name="Leaderboards"),
    path("",views.HomePage, name ="Home"),
    path("Contact/",views.ContactPage, name ="Contact"),
    path("Profil/",views.ProfilPage, name ="Profil"),
    path("Header/",lambda x : x, name ="Header"),
    # path('', views.Index.as_view(), name='index'),
    path('SignUp/', views.SignUp, name='SignUp'),
    path('Login/', views.Login, name='Login'),
    path('LogOut/', views.Logout, name='Logout'),
    path('Memory/', views.MemoryGame, name="MemoryGame"),
    path('ParseGameResults', views.ParseGameResults, name="ParseGameResults"),
    path('Us', views.UsPage, name="Us"),
]



