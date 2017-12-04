# """Test user registration."""
#
# from django.test import Client
# import pytest
#
#
# @pytest.fixture(scope='session')
# def bob():
#     """User Bob."""
#     c = Client()
#     response = c.post('/login/', {'username': 'bob', 'password': '7890uiop', 'email': 'bob@bob.bob'})
#     return response
#
#
# def test_bob(bob):
#     """"."""
#     import pdb; pdb.set_trace()
