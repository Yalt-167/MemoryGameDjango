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
    path("leaderboard/", views.LeaderboardPage, name="leaderboard"),
    # path("inscription/",views.inscription, name ="inscription"),
    # path("connexion/",connexion, name ="connexion"),
    path("about/",views.AboutPage, name ="about"),
    path("contact/",views.ContactPage, name ="contact"),
    path("header/",lambda x : x, name ="header"),
    # path('', views.Index.as_view(), name='index'),
    path('Login/', views.login_user, name='login'),
    path('SignUp/', views.sign_up, name='sign_up'),
    path('LogOut/', views.LogOut, name='LogOut'),
]


