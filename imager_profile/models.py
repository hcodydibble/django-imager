from django.db import models
from django.contrib.auth.models import User

SLR = 'SLR'
R_FIND = 'Range finder'
TWIN = 'Twin reflex'
WED = 'WEDDING'
PAP = 'PAPARAZZI'
BW = 'BLACK AND WHITE'
COLOR = 'COLOR'
SHOP = 'PHOTOSHOP'


# Create your models here.


class ImagerProfile(models.Model):
    CAMERA_CHOICES = (
        (SLR, 'SLR'),
        (R_FIND, 'Range finder'),
        (TWIN, 'Twin reflex')
    )
    SERVICE_CHOICES = (
        (WED, 'Wedding'),
        (PAP, 'Paparazzi')
    )
    STYLE_CHOICES = (
        (BW, 'Black and White'),
        (COLOR, 'Color'),
        (SHOP, 'Photoshop')
    )
    website = models.CharField(max_length=150, blank=True, null=True)
    location = models.CharField(max_length=200, blank=True, null=True)
    fee = models.FloatField(max_length=6, blank=True, null=True)
    camera = models.CharField(max_length=15, choices=CAMERA_CHOICES)
    services = models.CharField(max_length=20, choices=SERVICE_CHOICES)
    bio = models.TextField(max_length=200, blank=True, null=True)
    phone = models.CharField(max_length=11, blank=True, null=True)
    photo_style = models.CharField(max_length=20, choices=STYLE_CHOICES)
    user = models.OneToOneField(User, related_name='profile')
