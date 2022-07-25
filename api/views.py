from rest_framework.response import Response 
from rest_framework import status
from .serializers import PokemonSerializer
from rest_framework.decorators import api_view
from pokemon.models import Pokemon 

@api_view(['GET'])
def getData(requests):
    pokemon = Pokemon.objects.all()
    serializer = PokemonSerializer(pokemon, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addPokemon(requests):
    serializer = PokemonSerializer(data=requests.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET', 'PUT', 'DELETE'])
def pokemonDetails(requests, pk):
    try:
        pokemon = Pokemon.objects.get(pk=pk)
    except pokemon.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if requests.method == 'GET':
        serializer = PokemonSerializer(pokemon)
        return Response(serializer.data)

    elif requests.method == 'PUT':
        serializer = PokemonSerializer(pokemon, data=requests.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,
            status=status.HTTP_400_BAD_REQUEST)
    
    elif requests.method == 'DELETE':
        pokemon.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)