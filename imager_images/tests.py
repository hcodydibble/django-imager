from __future__ import unicode_literals

from django.contrib.auth.models import User

from datetime import datetime

from django.test import TestCase

from .models import Photo, Album

import factory

# Create your tests here.


class UserFactory(factory.django.DjangoModelFactory):
    """."""

    class Meta:
        """."""

        model = User

    username = 'bob'
    email = 'bob@example.com'


class ProfileTestCase(TestCase):

    def setUp(self):
        self.user = UserFactory.create()
        self.user.album.create(title='Title',
                               description='This is my album.',
                               )
        self.user.photo.create(title='A photo',
                               description='This is a photo.')

    def tearDown(self):
        User.objects.get(username='bob').delete()

    def test_bob_album_title_exists(self):
        album = self.user.album.get(title='Title')
        assert album.title == 'Title'

    def test_bob_album_description_exists(self):
        """."""
        album = self.user.album.get(title='Title')
        assert album.description == 'This is my album.'

    def test_bob_photo_title_exists(self):
        """."""
        photo = self.user.photo.get(title='A photo')
        assert photo.title == 'A photo'

    def test_bob_photo_description_exists(self):
        """."""
        photo = self.user.photo.get(title='A photo')
        assert photo.description == 'This is a photo.'

    def test_bob_datetime_exists(self):
        """."""
        album = self.user.album.get(title='Title')
        assert isinstance(album.date_created, datetime)

    def test_bob_photo_datetime_exists(self):
        """."""
        photo = self.user.photo.get(title='A photo')
        assert isinstance(photo.date_uploaded, datetime)

    def test_album_in_album_objects(self):
        """."""
        assert Album.objects.get(title='Title').description == 'This is my album.'

    def test_photo_in_photo_objects(self):
        """."""
        assert Photo.objects.get(title='A photo').description == 'This is a photo.'
