from django.db import models
from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator
from CalisthenicsWorkoutTracker.workouts.validators import validate_workout_name
from CalisthenicsWorkoutTracker.programs.models import Program
from django.contrib.auth import get_user_model

UserModel = get_user_model()


class Workout(models.Model):
    DIFFICULTY_CHOICES = [
        ('Novice', 'Novice'),
        ('Beginner', 'Beginner'),
        ('Intermediate', 'Intermediate'),
        ('Advanced', 'Advanced'),
        ('Mastery', 'Mastery'),
    ]

    MAX_DIFFICULTY_LENGTH = 15
    MAX_NAME_LENGTH = 30
    MIN_NAME_LENGTH = 3
    MAX_DESCRIPTION_LENGTH = 200
    MAX_DURATION_LENGTH = 90
    MIN_DURATION_LENGTH = 30

    name = models.CharField(
        max_length=MAX_NAME_LENGTH,
        #unique=True,
        validators=[MinLengthValidator(MIN_NAME_LENGTH), validate_workout_name],
        verbose_name="Workout Name",
        blank=False,
        null=False,
    )

    difficulty = models.CharField(
        max_length=MAX_DIFFICULTY_LENGTH,
        choices=DIFFICULTY_CHOICES,
        verbose_name="Difficulty",
        blank=False,
        null=False,
    )

    description = models.TextField(
        max_length=MAX_DESCRIPTION_LENGTH,
        verbose_name="Description",
        blank=True,
        null=True,
    )

    duration = models.IntegerField(
        verbose_name="Duration (minutes)",
        help_text="Minimum 30, Maximum 90",
        validators=[MinValueValidator(MIN_DURATION_LENGTH), MaxValueValidator(MAX_DURATION_LENGTH)],
        blank=False,
        null=False,
    )

    image_url = models.URLField(
        verbose_name="Image URL",
        blank=True,
        null=True,
    )

    program = models.ForeignKey(
        to=Program,
        on_delete=models.CASCADE,
        related_name="workouts_set",
        verbose_name="Program",
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name
