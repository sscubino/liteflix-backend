from movies.models import Movie, BackdropImage
from rest_framework import serializers


class BackdropImageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BackdropImage
        fields = ['id', 'file']

class MovieSerializer(serializers.HyperlinkedModelSerializer):
    backdrop = serializers.PrimaryKeyRelatedField(many=False,
                                                  queryset=BackdropImage.objects.all(),
                                                  write_only=True)
    backdrop_url = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Movie
        fields = ['title', 'backdrop', 'backdrop_url']

    def get_backdrop_url(self, movie):
        request = self.context.get('request')
        backdrop_url = movie.backdrop.file.url
        return request.build_absolute_uri(backdrop_url)
    