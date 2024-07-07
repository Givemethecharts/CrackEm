from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from CrackEm.accounts.managers import AppUserManager
from CrackEm.accounts.validators import validate_profile_picture, username_validator


# Auth user fields

class AppUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(null=False, blank=False, unique=True)
    first_name = models.CharField(max_length=30, blank=False, null=False)
    last_name = models.CharField(max_length=30, blank=False, null=False)
    username = models.CharField(max_length=30, blank=False, null=False, unique=True,
                                validators=[username_validator])

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    date_joined = models.DateTimeField(auto_now_add=True)

    objects = AppUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def __str__(self):
        return self.email


# User Data
class Profile(models.Model):
    to_user = models.OneToOneField(to=AppUser, on_delete=models.CASCADE, primary_key=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True,
                                        validators=[validate_profile_picture])
    age = models.IntegerField(null=True, blank=True)
