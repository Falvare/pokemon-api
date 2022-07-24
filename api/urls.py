from django.urls import path
from .views import getData, addPokemon

urlpatterns = [
    path('', getData),
    path('add-pokemon/', addPokemon),
]
