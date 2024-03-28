from CalisthenicsWorkoutTracker.meal_plans.models import MealPlan
from django import forms


class MealPlanEditForm(forms.ModelForm):

    class Meta:
        model = MealPlan
        fields = ['name', 'description', 'meal_plan_type', 'goal_calories', 'image_url']
        labels = {
            'name': 'Meal Plan Name:',
            'description': 'Description:',
            'meal_plan_type': 'Meal Plan Type:',
            'goal_calories': 'Goal Calories:',
            'image_url': 'Meal Plan Picture:',
        }
