"""Views for the Django Imager Site."""
import random
import os
from django.shortcuts import render
from django.conf import settings
from django.contrib.auth.models import User


def home_view(request):
    """The home view."""
    list_images = os.listdir(path=settings.MEDIA_ROOT)
    choice = random.choice(list_images)
    return render(request, 'django_imager/homepage.html', {'choice': choice})

# 
# def profile_view(request):
#     """The profile view."""
#     username = request.user.username
#     profile = User.objects.get(username=username)
#     return render(request, 'django_imager/profile.html', {'profile': profile})
