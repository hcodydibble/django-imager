"""Profile url."""

from django.conf.urls import url
from imager_profile.views import profile_view

urlpatterns = [
    url(r'^$', profile_view, name='profile'),
    url(r'^(?P<user_search>\w+)', profile_view),
]
