"""Profile url."""

from django.conf.urls import url
from imager_profile.views import profile_view, home_profile

urlpatterns = [
    url(r'^profile/(?P<username>)', profile_view, name='profile'),
    url(r'^$', home_profile, name='profile_home'),
]
