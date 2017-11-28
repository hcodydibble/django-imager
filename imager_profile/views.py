from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.


def home_profile(request):
    pass


def profile_view(request):
    """The profile view."""
    username = request.user.username
    user = User.objects.get(username=username)
    profile = user.profile
    # import pdb; pdb.set_trace()
    return render(request, 'django_imager/profile.html', {'profile': profile})
