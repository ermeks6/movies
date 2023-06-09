from rest_framework import serializers

from movie.models import Movie


class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('id', 'title', 'preview')


class MovieRetrieveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = '__all__'

