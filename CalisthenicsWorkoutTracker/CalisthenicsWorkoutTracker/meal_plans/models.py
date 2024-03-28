from django.db import models
from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator
from CalisthenicsWorkoutTracker.meal_plans.validators import validate_meal_plan_name
from CalisthenicsWorkoutTracker.programs.models import Program
from django.contrib.auth import get_user_model

UserModel = get_user_model()


class MealPlan(models.Model):
    MEAL_PLAN_TYPE_CHOICES = [
        ('Bulk', 'Bulk'),
        ('Cut', 'Cut'),
        ('Other', 'Other'),
    ]

    MAX_NAME_LENGTH = 30
    MIN_NAME_LENGTH = 3
    MEAL_PLAN_NAME_MAX_LENGTH = 15
    MAX_DESCRIPTION_LENGTH = 200
    MAX_GOAL_CALORIES = 4000
    MIN_GOAL_CALORIES = 1000

    name = models.CharField(
        max_length=MAX_NAME_LENGTH,
        #unique=True,
        validators=[MinLengthValidator(MIN_NAME_LENGTH), validate_meal_plan_name],
        verbose_name="Meal Plan Name",
        blank=False,
        null=False,
    )

    description = models.TextField(
        max_length=MAX_DESCRIPTION_LENGTH,
        verbose_name="Description",
        blank=True,
        null=True,
    )

    meal_plan_type = models.CharField(
        max_length=MEAL_PLAN_NAME_MAX_LENGTH,
        choices=MEAL_PLAN_TYPE_CHOICES,
        verbose_name="Meal Plan Type",
        blank=False,
        null=False,
    )

    goal_calories = models.PositiveIntegerField(
        verbose_name="Goal Calories",
        validators=[MinValueValidator(MIN_GOAL_CALORIES), MaxValueValidator(MAX_GOAL_CALORIES)],
        help_text="Goal calories/day",
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
        related_name="meal_plans_set",
        verbose_name="Program",
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name
