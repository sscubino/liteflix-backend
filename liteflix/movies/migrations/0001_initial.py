# Generated by Django 4.1.4 on 2022-12-28 21:19

from django.db import migrations, models
import django.db.models.deletion
import movies.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BackdropImage',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('file', models.ImageField(upload_to=movies.models.upload_image_to)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('backdrop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.backdropimage')),
            ],
        ),
    ]