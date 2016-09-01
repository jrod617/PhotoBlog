""" User models."""
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from . import GENDER_CHOICES, US_STATES_TERR, ORIGIN_COUNTRY_CHOICES

class ChasinViewsUser(AbstractUser):

    """
    ChasinViews specific subclass of AbstractUser.

    """

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'

    gender = models.BooleanField(default=1, blank=False, choices = GENDER_CHOICES)
    
    birth_date = models.DateField(_("Birth Date"), default=timezone.now, blank=True)
    
    state = models.CharField(max_length=2, choices=US_STATES_TERR, default=US_STATES_TERR[0][0])
    city = models.CharField(max_length=250,default='')
    
    countryOfOrigin = models.CharField(max_length=3, null=False, default=ORIGIN_COUNTRY_CHOICES[0][0], choices=ORIGIN_COUNTRY_CHOICES )