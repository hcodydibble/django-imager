"""Production settings."""
from settings import *

DEBUG = False
TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ['http://ec2-52-10-91-51.us-west-2.compute.amazonaws.com', 'localhost']

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
