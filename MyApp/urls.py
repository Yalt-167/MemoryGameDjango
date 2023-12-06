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
    path("", views.Home, name="Home"),
    # path("", views.DisplayUsers, name="DisplayUsers"),
    path("leaderboard/", views.leaderboard, name="leaderboard"),
    path("inscription/",views.inscription, name ="inscription"),
    # path("connexion/",connexion, name ="connexion"),
    path("about/",views.about, name ="about"),
    path("contact/",views.contact, name ="contact"),
    path("header/",lambda x : x, name ="header"),
    # path('', views.Index.as_view(), name='index'),
    path('Login/', views.login_user, name='login'),
    path('inscription/', views.sign_up, name='sign_up'),
]


