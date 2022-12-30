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
    backdrop_path = serializers.CharField(read_only=True)

    class Meta:
        model = Movie
        fields = ['title', 'backdrop', 'backdrop_path']