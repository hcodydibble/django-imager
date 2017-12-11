from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from multiselectfield import MultiSelectField as multi

SLR = 'SLR'
R_FIND = 'Range finder'
TWIN = 'Twin reflex'
WED = 'WEDDING'
PAP = 'PAPARAZZI'
BW = 'BLACK&WHITE'
COLOR = 'COLOR'
SHOP = 'PHOTOSHOP'


class ProfileManager(models.Manager):
    """."""

    def get_queryset(self):
        """."""
        return super(ProfileManager, self).get_queryset().filter(user__is_active=True)
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
    services = multi(choices=SERVICE_CHOICES, max_choices=2)
    bio = models.TextField(max_length=200, blank=True, null=True)
    photo_style = multi(choices=STYLE_CHOICES, max_choices=3)
    phone = models.CharField(max_length=12, blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    active = ProfileManager()
    objects = models.Manager()

    @property  # pragma no cover
    def is_active(self):
        """."""
        return self.user.is_active


@receiver(post_save, sender=User)
def create_user_imager_profile(sender, instance, created, **kwargs):
    if created:
        ImagerProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_imager_profile(sender, instance, **kwargs):
    instance.profile.save()
