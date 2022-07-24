from rest_framework.response import Response 
from .serializers import PokemonSerializer
from rest_framework.decorators import api_view
from pokemon.models import Pokemon 

@api_view(['GET'])
def getData(requests):
    pokemon = Pokemon.objects.all()
    serializer = PokemonSerializer(pokemon, many=True)
    return Response(requests, serializer.data)