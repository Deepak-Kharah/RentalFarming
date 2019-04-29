from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

allowed_exceptional_phone_number = (123,)


def phone_number_length_validator(value):
    if not str(value).isdigit() or (len(str(value)) != 10 and str(value) not in allowed_exceptional_phone_number):
        raise ValidationError(_('Phone number is not valid.'))
