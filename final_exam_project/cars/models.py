from django.core import validators
from django.db import models

from final_exam_project.core_app.validators import ValueInRangeValidator, validate_file_less_than_2mb


class Cars(models.Model):
    TYPE_MAX_LEN = 10
    TYPE_CHOICES = ["Hatchback", "Sedan", "Crossover", "Minibus"]
    MODEL_MIN_LEN = 2
    MODEL_MAX_LEN = 20
    YEAR_MIN_VALUE = 1980
    YEAR_MAX_VALUE = 2049
    FUEL = ["Gasoline", "Diesel", "LPG", "Electric"]
    PRICE_MIN_VALUE = 1
    PASSENGERS_MIN = 1
    PASSENGERS_MAX = 6

    type = models.CharField(
        blank=False,
        null=False,
        choices=[(choice.upper(), choice) for choice in TYPE_CHOICES],
        max_length=max([len(choice) for choice in TYPE_CHOICES]),
    )

    model = models.CharField(
        blank=False,
        null=False,
        max_length=MODEL_MAX_LEN,
        validators=(
            validators.MinLengthValidator(MODEL_MIN_LEN),
        ),
    )

    year = models.PositiveIntegerField(
        blank=False,
        null=False,
        validators=(
            ValueInRangeValidator(YEAR_MIN_VALUE, YEAR_MAX_VALUE, message=f'Year must be between {YEAR_MIN_VALUE} and {YEAR_MAX_VALUE}'),
        ),
    )
    passengers = models.PositiveIntegerField(
        blank=False,
        null=False,
        validators=(
            ValueInRangeValidator(PASSENGERS_MIN, PASSENGERS_MAX, message=f'Passengers must be between {PASSENGERS_MIN} and {PASSENGERS_MAX}'),
        ),
    )

    fuel = models.CharField(
        blank=False,
        null=False,
        choices=[(choice.upper(), choice) for choice in FUEL],
        max_length=max([len(choice) for choice in FUEL]),
    )

    photo = models.ImageField(
        blank=False,
        null=False,
        upload_to='mediafiles/user_photos/',
        validators=(validate_file_less_than_2mb,)
    )

    price_per_day = models.FloatField(
        blank=False,
        null=False,
        validators=(
            validators.MinValueValidator(PRICE_MIN_VALUE),
        )
    )

    def __str__(self):
        return self.model
