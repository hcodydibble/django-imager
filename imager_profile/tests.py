"""Django imager_profile test."""

from __future__ import unicode_literals

from django.contrib.auth.models import User

from django.test import TestCase

import factory

from django.test import Client

import pytest


class UserFactory(factory.django.DjangoModelFactory):
    """."""

    class Meta:
        """."""

        model = User

    username = 'bob'
    email = 'bob@example.com'


class ProfileTestCase(TestCase):
    """ProfileTestCase 1."""

    def setUp(self):
        """Setup user bob."""
        self.user = UserFactory.create()
        self.user.set_password('secret')
        self.user.website = 'https://bob.net'
        self.user.location = 'Seattle, WA'
        self.user.fee = 120
        self.user.camera = 'Nikon D850'
        self.user.services = 'All'
        self.user.bio = 'No need'
        self.user.phone = '555-555-5555'
        self.user.photo_style = 'All'
        self.user.user = 'bob'
        self.user.save()
        self.client = Client()
        self.bob = self.client.post('/login/', {'username': 'bob', 'password': '7890uiop'})


    @pytest.fixture
    def bob(self):
        """User Bob."""
        client = Client()
        self.response = client.post('/login/', {'username': 'bob', 'password': '7890uiop'})
        return response

    def test_user_creation_bob(self):
        """Test_user_creation username bob."""
        assert self.user.username == 'bob'

    def test_user_creation_email(self):
        """Test_user_creation username bob."""
        assert self.user.email == 'bob@example.com'

    def test_user_creation_pw_hash(self):
        """Test_user_creation pw hash bob."""
        assert self.user.password is not 'pbkdf2_sha256$36000$pMxN1crrDp6Y$rbJ5x0bTo3yRhEsk6Iln+s/jXZQ+MtenGrKNqenffOE'

    def test_user_creation_website(self):
        """Test_user_creation website bob."""
        assert self.user.website == 'https://bob.net'

    def test_user_creation_is_active(self):
        """Test_user_creation is active bob."""
        assert self.user.is_active is True

    def test_user_creation_location(self):
        """Test_user_creation location bob."""
        assert self.user.location == 'Seattle, WA'

    def test_user_creation_fee(self):
        """Test_user_creation fee bob."""
        assert self.user.fee == 120

    def test_user_creation_camera(self):
        """Test_user_creation camera bob."""
        assert self.user.camera == 'Nikon D850'

    def test_user_creation_services(self):
        """Test_user_creation services bob."""
        assert self.user.services == 'All'

    def test_user_is_active(self):
        """Test all active users are listed."""
        assert self.user.profile.active() == ['bob']

    def test_bob_is_active(bob):
        """"Test bob is active."""
        assert bob.user.is_active is True

    def test_response_contains_empty_title(self):
        """"Test_response_contains_empty_title."""
        client = Client()
        response = client.get('/')
        assert b'<title>IMAGER</title>' in response.content

    def test_response_contains_login_title(self):
        """"Test_response_contains_login_title."""
        client = Client()
        response = client.get('/login/')
        assert b'<title>Login</title>' in response.content

    def test_response_contains_register_title(self):
        """"Test_response_contains_register_title."""
        client = Client()
        response = client.get('/accounts/register/')
        assert b'<title>Register</title>' in response.content

    def test_response_contains_registered_title(self):
        """"Test_response_contains_registered_title."""
        client = Client()
        response = client.get('/accounts/register/complete/')
        assert b'<title>Registered</title>' in response.content

    def test_response_contains_hooray_title(self):
        """"test_response_contains_hooray_title."""
        client = Client()
        response = client.get('/accounts/activate/complete/')
        assert b'<title>Hooray!</title>' in response.content

    def test_response_register_redirects(self):
        """"Test_response_contains_register_title."""
        client = Client()
        response = client.post('/accounts/register/',
                               {'username': 'fred',
                                'email': 'fred@fred.com',
                                'password1': '7890uiop',
                                'password2': '7890uiop'})
        assert response.url == '/accounts/register/complete/'

    def test_profile_view_shows_bob(self):
        """test_profile_view_shows_bob."""
        response = self.client.get('/profile/bob/')
        assert b'<li>username: bob</li>' in response.content

    def test_profile_view_shows_(self):
        """test_profile_view_shows_."""
        self.client.post('/login/', {'username': 'bob', 'password': '7890uiop'})
        response = self.client.get('/profile')
        # import pdb; pdb.set_trace()
        assert response.content == b''
