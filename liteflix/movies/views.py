from movies.serializers import BackdropImageSerializer, MovieSerializer
from movies.models import Movie, BackdropImage
from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser, FormParser


class MoviesViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    http_method_names = ['get', 'post', 'head']


class BackdropImageViewSet(viewsets.ModelViewSet):
    parser_classes = (MultiPartParser, FormParser)
    queryset = BackdropImage.objects.all()
    serializer_class = BackdropImageSerializer
    http_method_names = ['post', 'head']
