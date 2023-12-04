from django.urls import path
from . import views
# from .views import classement_view
from .views import leaderboard
from .views import inscription


urlpatterns = [
    path("", views.Home, name="Home"),
    # path("", views.DisplayUsers, name="DisplayUsers"),
    path('leaderboard/', leaderboard, name='leaderboard'),
    path("",views.inscription, name ="inscription"),
   
]


