"""Django imager_profile test."""

from __future__ import unicode_literals

from django.contrib.auth.models import User

from django.test import TestCase

import factory

from django.test import Client

from .models import ImagerProfile as IP

from imager_images.views import LibraryView


class UserFactory(factory.django.DjangoModelFactory):
    """."""

    class Meta:
        """."""

        model = User

    username = 'bob'
    email = 'bob@example.com'


class User2Factory(factory.django.DjangoModelFactory):
    """."""

    class Meta:
        """."""

        model = User

    username = 'bill'
    email = 'bill@example.com'


class ProfileTestCase(TestCase):
    """ProfileTestCase 1."""

    def setUp(self):
        """Setup user bob."""
        self.user = UserFactory.create()
        self.user.set_password('secret')
        self.user.profile.website = 'https://bob.net'
        self.user.profile.location = 'Seattle, WA'
        self.user.profile.fee = 120
        self.user.profile.camera = 'Nikon D850'
        self.user.profile.services = 'All'
        self.user.profile.bio = 'No need'
        self.user.profile.phone = '555-555-5555'
        self.user.profile.photo_style = 'All'
        self.user.profile.save()
        self.bob = IP.objects.get(id=self.user.pk)
        self.phil = User(username='phil', email='p@p.com', is_active=False)
        self.active = IP.active.all()

    def tearDown(self):
        """."""
        User.objects.all().delete()

    def test_user_creation_bob(self):
        """Test_user_creation username bob."""
        assert User.objects.get(username='bob').username == 'bob'

    def test_user_creation_email(self):
        """Test_user_creation username bob."""
        assert self.bob.user.email == 'bob@example.com'

    def test_user_creation_pw_hash(self):
        """Test_user_creation pw hash bob."""
        assert self.bob.user.password is not 'pbkdf2_sha256$36000$pMxN1crrDp6Y$rbJ5x0bTo3yRhEsk6Iln+s/jXZQ+MtenGrKNqenffOE'

    def test_user_creation_website(self):
        """Test_user_creation website bob."""
        assert self.bob.website == 'https://bob.net'

    def test_user_creation_is_active(self):
        """Test_user_creation is active bob."""
        assert self.bob.is_active is True

    def test_user_creation_location(self):
        """Test_user_creation location bob."""
        assert self.bob.location == 'Seattle, WA'

    def test_user_creation_fee(self):
        """Test_user_creation fee bob."""
        assert self.bob.fee == 120

    def test_user_creation_camera(self):
        """Test_user_creation camera bob."""
        assert self.bob.camera == 'Nikon D850'

    def test_user_creation_services(self):
        """Test_user_creation services bob."""
        assert self.bob.services == ['All']

    def test_bob_is_active(self):
        """"Test bob is active."""
        # assert self.bob.is_active is True

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
        fred = User.objects.get(username='fred')
        assert fred.username == 'fred'
        assert response.url == '/accounts/register/complete/'

    def test_profile_view_shows_bob(self):
        """test_profile_view_shows_bob."""
        response = self.client.get('/profile/bob')
        assert b'<li>username: bob</li>' in response.content

    def test_profile_view_shows_(self):
        """test_profile_view_shows_."""
        self.client.post('/login/', {'username': 'bob', 'password': '7890uiop'})
        response = self.client.get('/profile')
        assert response.content == b''

    def test_user_is_active(self):
        """Test all active users are listed."""
        assert IP.active.get(id=self.bob.user_id).user.username == 'bob'

    def test_user_is_not_active(self):
        """."""
        assert IP.active.all().count() == 1

    def test_add_another_active_user(self):
        """."""
        self.bill = User2Factory.create()
        assert IP.active.all().count() == 2

    def test_library_view_get_queryset(self):
        """."""
        bob = self.client.post('/login/',
                               {'username': 'bob', 'password': '7890uiop'})
        response = LibraryView()
        assert response.template_name == 'django_imager/library.html'

    def test_update_profile(self):
        """."""

        client = Client()
        user = User
        user = User.objects.first()
        client.force_login(user)
        client.get('/profile/edit/')

        import pdb; pdb.set_trace()
