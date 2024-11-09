import re

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def phone_validator(phone):
    regex = r"^(\+?998)?[0-9]{9}$"
    if not re.match(regex, phone):
        raise ValidationError(_("Phone number is not valid"), code="invalid")
