from django.contrib import admin
from imager_images.models import Photo, Album
# Register your models here.
from .models import Photo, Album

admin.site.register(Photo)
admin.site.register(Album)
