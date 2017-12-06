"""Views for the Django Imager Site."""
import random
from django.shortcuts import render
from imager_images.models import Photo


def home_view(request):
    """The home view."""
    list_images = Photo.objects.all()
    if list_images:
        choice = random.choice(list_images).image_file
    choice = 'ryan.jpg'
    return render(request, 'django_imager/homepage.html', {'choice': choice})
