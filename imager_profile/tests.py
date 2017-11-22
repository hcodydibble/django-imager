"""Django imager_profile test."""

from __future__ import unicode_literals

from django.contrib.auth.models import User

from django.test import TestCase

import factory

from django.test import Client

import pytest





class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
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
        # import pdb; pdb.set_trace()

    @pytest.fixture
    def bob():
        """User Bob."""
        client = Client()
        response = client.post('/login/', {'username': 'bob', 'password': '7890uiop'})
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
        import pdb; pdb.set_trace()
        
        assert bob.user.is_active is True
