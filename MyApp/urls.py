from django.urls import path
from . import views

urlpatterns = [
    path("", views.Home, name="Home"),
    # path("", views.DisplayUsers, name="DisplayUsers"),
]

from django.urls import path
from .views import memory_game

urlpatterns = [
    path('memory-game/', memory_game, name='memory_game'),
]

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('game/', include('game.urls')),
]