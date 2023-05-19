from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

from movie.models import Movie
from movie.serializers import MovieSerializer, MovieRetrieveSerializer


@api_view(['GET'])
def hello_api_view(request):
    return Response(data={'message': 'Hello, its my first Rest API Response'},
                    status=status.HTTP_200_OK)


@api_view(['GET'])
def movie_list_api_view(request):
    movie = Movie.objects.all()

    data = MovieSerializer(movie, many=True).data

    return Response(data=data, status=status.HTTP_200_OK)


@api_view(['GET'])
def movie_retrieve_api_view(request, **kwargs):
    movie = Movie.objects.get(id=kwargs['id'])

    data = MovieRetrieveSerializer(movie, many=False).data

    return Response(data=data, status=status.HTTP_200_OK)




