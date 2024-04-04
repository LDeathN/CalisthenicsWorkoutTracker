from django.contrib import admin
from CalisthenicsWorkoutTracker.meals.models import Meal


@admin.register(Meal)
class MealAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'meal_type', 'meal_name_type', 'calories')
    list_filter = ('meal_type', 'meal_plan')
    search_fields = ('name', 'meal_plan__name')

