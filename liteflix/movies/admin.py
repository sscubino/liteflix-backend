from django.contrib import admin

from movies.models import BackdropImage, Movie

admin.site.register(Movie)
admin.site.register(BackdropImage)
