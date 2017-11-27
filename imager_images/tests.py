from __future__ import unicode_literals

from django.contrib.auth.models import User

from django.test import TestCase

import factory

from django.test import Client

import pytest

import datetime

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
        self.user.album.create(album_title='Title',
                               album_description='This is my album.',
                               )
        self.user.photo.create(title='A photo',
                               description='This is a photo.')

    def tearDown(self):
        User.objects.get(username='bob').delete()

    def test_bob_album_title_exists(self):
        album = self.user.album.get(album_title='Title')
        assert album.album_title == 'Title'

    def test_bob_album_description_exists(self):
        album = self.user.album.get(album_title='Title')
        assert album.album_description == 'This is my album.'

    def test_bob_photo_title_exists(self):
        photo = self.user.photo.get(title='A photo')
        assert photo.title == 'A photo'

    def test_bob_photo_description_exists(self):
        photo = self.user.photo.get(title='A photo')
        assert photo.description == 'This is a photo.'

    def test_bob_album_datetime_exists(self):
        album = self.user.album.get(album_title='Title')
        assert isinstance(album.date_created, datetime.datetime)

    def test_bob_photo_datetime_exists(self):
        photo = self.user.photo.get(title='A photo')
        assert isinstance(photo.date_uploaded, datetime.datetime)
