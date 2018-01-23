"""."""

from __future__ import unicode_literals

from django.contrib.auth.models import User

import datetime

from django.test import TestCase

from .models import Photo, Album

import factory

from django_imager.views import HomeView

from django.urls import reverse_lazy

from bs4 import BeautifulSoup

from .views import LibraryView, AlbumView, PhotoView, PublicPhotos, PublicAlbums, AlbumEditView


class UserFactory(factory.django.DjangoModelFactory):
    """."""

    class Meta:
        """."""

        model = User

    username = 'bob'
    email = 'bob@example.com'


class ProfileTestCase(TestCase):
    """."""

    def setUp(self):
        """."""
        self.user = UserFactory.create()
        self.user.set_password('7890uiop')
        self.user.save()
        self.user.album.create(
            title='Title',
            description='This is my album.',
        )
        self.user.photo.create(
            title='A photo',
            description='This is a photo.',
            image_file='django_imager/MEDIA/ryan.jpg'
        )

        self.chris = User.objects.create_superuser(
            'chris',
            'c@c.com',
            '7890uiop'
        )
        self.client.login(username='chris', password='7890uiop')

    def tearDown(self):
        """."""
        User.objects.get(username='bob').delete()

    def test_bob_album_title_exists(self):
        """."""
        album = self.user.album.get(title='Title')
        assert album.title == 'Title'

    def test_bob_album_description_exists(self):
        """."""
        album = self.user.album.get(title='Title')
        assert album.description == 'This is my album.'

    def test_add_another_album(self):
        """."""
        self.user.album.create(
            title='Title2',
            description='This is my second album.',
        )
        assert Album.objects.count() == 2

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
        assert isinstance(album.date_created, datetime.datetime)

    def test_bob_photo_datetime_exists(self):
        """."""
        photo = self.user.photo.get(title='A photo')
        assert isinstance(photo.date_uploaded, datetime.datetime)

    def test_album_in_album_objects(self):
        """."""
        assert Album.objects.get(
            title='Title'
        ).description == 'This is my album.'

    def test_photo_in_photo_objects(self):
        """."""
        assert Photo.objects.get(
            title='A photo'
        ).description == 'This is a photo.'

    def test_profile_view_shows_bob(self):
        """test_profile_view_shows_bob."""
        response = self.client.get('/profile/bob')
        assert b'<li>username: bob</li>' in response.content

    def test_home_view_has_title(self):
        """."""
        response = HomeView()
        assert response.template_name == 'django_imager/homepage.html'

    def test_library_view_correct_template(self):
        """."""
        response = LibraryView()
        assert response.template_name == 'django_imager/library.html'

    def test_album_view_correct_template(self):
        """."""
        response = AlbumView()
        assert response.template_name == 'django_imager/album.html'

    def test_photo_view_correct_template(self):
        """."""
        response = PhotoView()
        assert response.template_name == 'django_imager/photo.html'

    def test_public_photos_view_correct_template(self):
        """."""
        response = PublicPhotos()
        assert response.template_name == 'django_imager/public_photo.html'

    def test_public_photos_view_queryset(self):
        """."""
        from django.db.models.query import QuerySet
        assert isinstance(PublicPhotos().get_queryset(), QuerySet)

    def test_public_albums_view_queryset(self):
        """."""
        from django.db.models.query import QuerySet
        assert isinstance(PublicAlbums().get_queryset(), QuerySet)

    def test_individual_album_page_contents(self):
        """Test that the single album page has content."""
        self.client.force_login(self.user)
        alb_id = Album.objects.first().id
        response = self.client.get(
            reverse_lazy('album', kwargs={'pk': alb_id})
        )
        html = BeautifulSoup(response.content, 'html.parser')
        self.assertEqual(1, len(html.findAll('img')))

    def test_bad_photo_request_page(self):
        """Test 404 on pk of photo that does not exist."""
        self.client.force_login(self.user)
        pic_id = Photo.objects.first().id + 100
        response = self.client.get(
            reverse_lazy('photo', kwargs={'pk': pic_id})
        )
        self.assertTrue(response.status_code == 404)
