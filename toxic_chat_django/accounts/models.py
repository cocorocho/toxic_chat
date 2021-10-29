from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from .validators import username_validator, not_allnum_validator


class User(AbstractUser):
    username = models.CharField(
        ('username'),
        validators=[username_validator, not_allnum_validator],
        error_messages={
            'unique': ("A user with that username already exists."),
        },
        unique=True,
        max_length=settings.MAX_USERNAME_LENGTH,
    )
    dark_mode = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Users"

    def __repr__(self) -> str:
        return self.username

    def __str__(self) -> str:
        return self.username
