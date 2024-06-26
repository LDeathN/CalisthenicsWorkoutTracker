from django.contrib import admin
from CalisthenicsWorkoutTracker.meal_plans.models import MealPlan


@admin.register(MealPlan)
class MealPlanAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'meal_plan_type', 'goal_calories')
    list_filter = ('program', 'meal_plan_type')
    search_fields = ('name', 'program__name')

