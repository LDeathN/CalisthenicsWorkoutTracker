from django.db import models
from django.core.validators import MinLengthValidator, MaxValueValidator
from CalisthenicsWorkoutTracker.meals.validators import validate_meal_name
from CalisthenicsWorkoutTracker.meal_plans.models import MealPlan
from django.contrib.auth import get_user_model

UserModel = get_user_model()


class Meal(models.Model):
    MEAL_TYPE_CHOICES = [
        ('Soup', 'Soup'),
        ('Main', 'Main'),
        ('Dessert', 'Dessert'),
        ('Drink', 'Drink'),
    ]

    MEAL_NAME_CHOICES = [
        ('Breakfast', 'Breakfast'),
        ('Lunch', 'Lunch'),
        ('Dinner', 'Dinner'),
        ('Snack', 'Snack'),
    ]

    MAX_NAME_LENGTH = 30
    MIN_NAME_LENGTH = 3
    MAX_DESCRIPTION_LENGTH = 200
    MAX_CALORIES_PER_MEAL = 2000
    MEAL_TYPE_MAX_LENGTH = 20
    MEAL_NAME_MAX_LENGTH = 20

    name = models.CharField(
        max_length=MAX_NAME_LENGTH,
        #unique=True,
        validators=[MinLengthValidator(MIN_NAME_LENGTH), validate_meal_name],
        verbose_name="Meal Name",
        blank=False,
        null=False,
    )

    calories = models.PositiveIntegerField(
        validators=[MaxValueValidator(MAX_CALORIES_PER_MEAL)],
        verbose_name="Calories",
        blank=False,
        null=False,
    )

    description = models.TextField(
        max_length=MAX_DESCRIPTION_LENGTH,
        verbose_name="Description",
        blank=True,
        null=True,
    )

    meal_type = models.CharField(
        max_length=MEAL_TYPE_MAX_LENGTH,
        choices=MEAL_TYPE_CHOICES,
        verbose_name="Meal Type",
        blank=False,
        null=False,
    )

    meal_name_type = models.CharField(
        max_length=MEAL_NAME_MAX_LENGTH,
        choices=MEAL_NAME_CHOICES,
        verbose_name="Meal Name Type",
        blank=False,
        null=False,
    )

    image_url = models.URLField(
        verbose_name="Image URL",
        blank=True,
        null=True,
    )

    carbohydrates = models.PositiveIntegerField(
        verbose_name="Carbohydrates",
        blank=True,
        null=True,
    )

    proteins = models.PositiveIntegerField(
        verbose_name="Proteins",
        blank=True,
        null=True,
    )

    fats = models.PositiveIntegerField(
        verbose_name="Fats",
        blank=True,
        null=True,
    )

    meal_plan = models.ForeignKey(
        to=MealPlan,
        on_delete=models.CASCADE,
        related_name="meals_set",
        verbose_name="MealPlan"
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name
