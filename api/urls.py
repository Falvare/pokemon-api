from django.urls import path
from .views import getData, addPokemon, pokemonDetails

urlpatterns = [
    path('', getData),
    path('add-pokemon/', addPokemon),
    path('pokemon/<int:pk>', pokemonDetails)
]
