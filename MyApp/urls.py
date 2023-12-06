from django.urls import path
from .views import Home, MemoryGame, ParseGameResults

urlpatterns = [
    path("", Home, name="Home"), # name -> associate a unique name to the path so u can refer to it using the name (in temlpates) or using reverse(name) (in regular python)
    path("Memory/", MemoryGame, name="Memory"),
    path("", ParseGameResults, name="ParseGameResults"),
]