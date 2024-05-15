import string
from random import choice

from django.db import models
from django.contrib.auth.models import AbstractUser

from .manager import UserManager


class User(AbstractUser):
    phone_number = models.CharField(max_length=11, unique=True)
    invite_code = models.CharField(max_length=6, blank=True, null=True)
    invited_by = models.ManyToManyField('self', blank=True, null=True)

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []
    objects = UserManager()

    def __str__(self):
        return self.phone_number
