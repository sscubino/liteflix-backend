from django.db import models
import uuid


def upload_image_to(instance, filename):
    file_ext = filename.split('.')[-1]
    return 'images/{filename}.{file_ext}'.format(filename=instance.pk, file_ext=file_ext)


class BackdropImage(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    file = models.ImageField(upload_to=upload_image_to)


class Movie(models.Model):
    title = models.CharField(max_length=300)
    backdrop = models.ForeignKey(BackdropImage, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def backdrop_path(self):
        return self.backdrop.file.url