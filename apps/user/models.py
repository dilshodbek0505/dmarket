from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from apps.user.validators import phone_validator
from apps.user.managers import UserManager
from apps.common.models import BaseModel




class User(AbstractUser, BaseModel):
    """
    Users within the Django authentication system are represented by this
    model.

    Username and password are required. Other fields are optional.
    """
    first_name = models.CharField(max_length=128, blank=True, verbose_name=_('First name'))
    last_name = models.CharField(max_length=128, blank=True, null=True, verbose_name=_('Last name'))
    phone_number = models.CharField(max_length=18, validators=[phone_validator],unique=True, verbose_name=_('Phone number'))
    profile = models.ImageField(upload_to='user_profile_image', blank=None, null=True, verbose_name=_('Profile photo'))
    telegram_id = models.IntegerField(default=0, verbose_name=_('Telegram id'))
    coints = models.PositiveBigIntegerField(default=0, verbose_name=_('Coins'))
    
    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ('first_name', )

    email = None
    date_joined = None
    username = None

    objects = UserManager()



    class Meta(AbstractUser.Meta):
        swappable = "AUTH_USER_MODEL"
    
    