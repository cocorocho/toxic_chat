from django.core import exceptions
from django.core.exceptions import ValidationError
from django.core import validators
from django.conf import settings
import re

def username_validator(username):
    pattern = r'^(?=.{4,16}$)(?![_.])(?!.*[_.]{2})[a-zA-Z0-9._]+(?<![_.])$'
    if not re.search(pattern, username):
        raise ValidationError(
            f"Username must have 4-16 characters, can not start and end with special characters"
        )


def not_allnum_validator(username):
    try:
        int(username)
        raise ValidationError(
            f"Password can not only contain numbers"
        )
    except ValueError:
        pass