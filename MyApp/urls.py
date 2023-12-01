from django.urls import path
from . import views

urlpatterns = [
    path("", views.Home, name="Home"),
    # path("DisplayUsers", views.DisplayUsers, name="DisplayUsers"),
    path('', views.MemoryGameView.as_view(), name='Memory'),
    path('flip_card/<int:card_id>/', views.flip_card, name='flip_card')
]