from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path("", views.Home, name="Home"),
    path("", views.DisplayUsers, name="DisplayUsers"),
    
]


