from django.db import models
from django.core.validators import MinLengthValidator, MaxValueValidator
from CalisthenicsWorkoutTracker.exercises.validators import validate_exercise_name, validate_repetitions
from CalisthenicsWorkoutTracker.workouts.models import Workout
from django.contrib.auth import get_user_model

UserModel = get_user_model()


class Exercise(models.Model):
    DIFFICULTY_CHOICES = [
        (1, 'Easy'),
        (2, 'Moderate'),
        (3, 'Intermediate'),
        (4, 'Challenging'),
        (5, 'Advanced'),
    ]

    MAX_NAME_LENGTH = 25
    MIN_NAME_LENGTH = 3
    MAX_DESCRIPTION_LENGTH = 200
    DEFAULT_REPETITIONS = 6
    MAX_REPETITIONS = 30

    name = models.CharField(
        max_length=MAX_NAME_LENGTH,
        #unique=True,
        validators=[MinLengthValidator(MIN_NAME_LENGTH), validate_exercise_name],
        verbose_name='Exercise Name',
        blank=False,
        null=False,
    )

    description = models.TextField(
        max_length=MAX_DESCRIPTION_LENGTH,
        verbose_name='Description',
        blank=True,
        null=True,
    )

    difficulty = models.IntegerField(
        choices=DIFFICULTY_CHOICES,
        verbose_name='Difficulty',
        help_text="1-5 (Easy to Advanced)",
        blank=False,
        null=False,
    )

    repetitions = models.PositiveIntegerField(
        default=DEFAULT_REPETITIONS,
        validators=[MaxValueValidator(MAX_REPETITIONS), validate_repetitions],
        verbose_name='Repetitions',
        blank=False,
        null=False,
    )

    workout = models.ForeignKey(
        to=Workout,
        on_delete=models.CASCADE,
        related_name='exercises_set',
        verbose_name='Workout',
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name
