"""Profile url."""

from django.conf.urls import url

urlpatterns = [
    url(r'^profile/(?P<username>)', name='profile'),
    url(r'^$', name='profile_home'),
]
