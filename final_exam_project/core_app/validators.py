from datetime import datetime

from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class ValueInRangeValidator:
    def __init__(self, min_value: float, max_value: float, message: str):
        self.min_value = min_value
        self.max_value = max_value
        self.message = message

    def __call__(self, value):
        if value < self.min_value or self.max_value < value:
            raise ValidationError(self.message)


def date_bigger_than_today(date):
    if date < datetime.today():
        raise ValidationError("The date cannot be in the past!")


def validate_only_letters(value):
    for ch in value:
        if not ch.isalpha():
            raise ValidationError('Only letters are allowed')


def megabytes_to_bytes(mb):
    return mb * 1024 * 1024


def validate_file_less_than_2mb(fileobj):
    filesize = fileobj.file.size
    megabyte_limit = 2.0
    if filesize > megabytes_to_bytes(megabyte_limit):
        raise ValidationError(f'Max file size is {megabyte_limit}MB')
