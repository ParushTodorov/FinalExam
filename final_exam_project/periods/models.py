from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.core import validators
from django.db import models
from final_exam_project.cars.models import Cars
from final_exam_project.core_app.validators import ValueInRangeValidator

UserModel = get_user_model()


class PeriodForRent(models.Model):
    CITY_MIN_LEN = 2
    CITY_MAX_LEN = 30
    ADDRESS_MIN_LEN = 2
    ADDRESS_MAX_LEN = 50
    COMMENT_MAX_LEN = 100
    TOTAL_PRICE_MIN = 0
    PROVINCE_CHOICES = ['South Eastern', 'South Central', 'South Western',
                        'North Eastern', 'North Central', 'North Western',
                        'Sofia']

    start_date = models.DateField(
        blank=False,
        null=False,
    )

    end_date = models.DateField(
        blank=False,
        null=False,
    )

    province = models.CharField(
        blank=False,
        null=False,
        choices=[(choice.upper(), choice) for choice in PROVINCE_CHOICES],
        max_length=max([len(choice) for choice in PROVINCE_CHOICES]),
    )

    city = models.CharField(
        blank=False,
        null=False,
        max_length=CITY_MAX_LEN,
        validators=(
            validators.MinLengthValidator(CITY_MIN_LEN),
        ),
    )

    address = models.CharField(
        blank=False,
        null=False,
        max_length=CITY_MAX_LEN,
        validators=(
            validators.MinLengthValidator(CITY_MIN_LEN),
        ),
    )

    comment = models.TextField(
        blank=True,
        null=True,
        max_length=COMMENT_MAX_LEN,
    )

    car = models.ForeignKey(
        Cars,
        null=False,
        blank=False,
        on_delete=models.CASCADE,
    )

    user = models.ForeignKey(
        UserModel,
        null=False,
        blank=False,
        on_delete=models.CASCADE,
    )

    total_price = models.FloatField(
        null=False,
        blank=False,
        validators=(
            validators.MinValueValidator(TOTAL_PRICE_MIN),
        ),
    )

    def __str__(self):
        return f'{self.car.model} from {self.start_date} to {self.end_date} - Price: {self.total_price} ' \
               f'Place: {self.city}, {self.address}'


class PeriodForPromo(models.Model):
    DISCOUNT_MIN = 1
    DISCOUNT_MAX = 100

    start_date = models.DateField(
        blank=False,
        null=False,
    )

    end_date = models.DateField(
        blank=False,
        null=False,
    )

    discount = models.FloatField(
        blank=False,
        null=False,
        validators={
            ValueInRangeValidator(DISCOUNT_MIN, DISCOUNT_MAX, 'Discount must be between 1 and 100!'),
        }
    )

    def __str__(self):
        return f'{self.discount} % discount from {self.start_date} to {self.end_date} '


class PeriodForPreparation(models.Model):
    DAYS_FOR_PREPARATION = 1
    PROVINCE_CHOICES = ['South Eastern', 'South Central', 'South Western',
                        'North Eastern', 'North Central', 'North Western',
                        'Sofia']

    province = models.CharField(
        unique=True,
        blank=False,
        null=False,
        choices=[(choice.upper(), choice) for choice in PROVINCE_CHOICES],
        max_length=max([len(choice) for choice in PROVINCE_CHOICES]),
    )

    days_for_preparation = models.PositiveIntegerField(
        blank=False,
        null=False,
        validators=(
            validators.MinValueValidator(DAYS_FOR_PREPARATION),
        ),
    )

    def __str__(self):
        return f'{self.province}'
