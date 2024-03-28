from django.db import models
from django.core.validators import MinLengthValidator
from CalisthenicsWorkoutTracker.programs.validators import validate_program_name
from django.contrib.auth import get_user_model

UserModel = get_user_model()


class Program(models.Model):
    MAX_NAME_LENGTH = 30
    MIN_NAME_LENGTH = 3
    MAX_DESCRIPTION_LENGTH = 200

    name = models.CharField(
        max_length=MAX_NAME_LENGTH,
        #unique=True,
        validators=[MinLengthValidator(MIN_NAME_LENGTH), validate_program_name],
        verbose_name="Program Name",
        blank=False,
        null=False,
    )

    description = models.TextField(
        max_length=MAX_DESCRIPTION_LENGTH,
        verbose_name="Description",
        blank=True,
        null=True,
    )

    start_date = models.DateField(
        verbose_name="Start Date",
        blank=False,
        null=False,
    )

    end_date = models.DateField(
        verbose_name="End Date",
        blank=False,
        null=False,
    )

    image_url = models.URLField(
        verbose_name="Image URL",
        blank=True,
        null=True,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name
