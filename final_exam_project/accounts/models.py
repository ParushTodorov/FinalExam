from django.contrib.auth import models as auth_models
from django.db import models
from django.core import validators

from final_exam_project.accounts.manager import AppUserManager
from final_exam_project.core_app.validators import validate_only_letters, validate_file_less_than_2mb


class AppUser(auth_models.AbstractUser, auth_models.PermissionsMixin):
    USERNAME_MIN_LEN = 3
    USERNAME_MAX_LEN = 30
    AGE_DEFAULT_VALUE = 18
    AGE_MIN_VALUE = 18
    FIRST_NAME_MIN_LEN = 1
    FIRST_NAME_MAX_LEN = 30
    LAST_NAME_MIN_LEN = 1
    LAST_NAME_MAX_LEN = 30
    CITY_MAX_LEN = 30

    username = models.CharField(
        max_length=USERNAME_MAX_LEN,
        unique=True,
        error_messages={
            "unique": "A user with that username already exists.",
        },
        validators=(
            validators.MinLengthValidator(USERNAME_MIN_LEN, message="The username must be a minimum of 2 chars"),
        ),
    )

    email = models.EmailField(
        unique=True,
        blank=False,
        null=False,
    )

    date_joined = models.DateTimeField(
        auto_now_add=True,
    )

    is_staff = models.BooleanField(
        default=False,
        null=False,
        blank=False,
    )

    age = models.IntegerField(
        default=AGE_DEFAULT_VALUE,
        blank=False,
        null=False,
        validators=(
            validators.MinValueValidator(AGE_MIN_VALUE),
        ),
    )

    first_name = models.CharField(
        blank=True,
        null=True,
        max_length=FIRST_NAME_MAX_LEN,
        validators=(
            validators.MinLengthValidator(FIRST_NAME_MIN_LEN),
            validate_only_letters,
        ),
    )

    last_name = models.CharField(
        blank=True,
        null=True,
        max_length=LAST_NAME_MAX_LEN,
        validators=(
            validators.MinLengthValidator(LAST_NAME_MIN_LEN),
            validate_only_letters,
        ),
    )

    city = models.CharField(
        blank=True,
        null=True,
        max_length=CITY_MAX_LEN,
    )

    phone_number = models.IntegerField(
        blank=True,
        null=True,
    )

    photo = models.ImageField(
        blank=True,
        null=True,
        upload_to='mediafiles/user_photos/',
        validators=(validate_file_less_than_2mb,)
    )

    objects = AppUserManager()

    def get_fullname(self):
        if self.first_name and self.last_name:
            return f'{self.first_name} {self.last_name}'

        if self.first_name:
            return f'{self.first_name}'

        if self.last_name:
            return f'{self.last_name}'
