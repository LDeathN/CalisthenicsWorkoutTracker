from CalisthenicsWorkoutTracker.meals.models import Meal
from django import forms


class MealEditForm(forms.ModelForm):

    class Meta:
        model = Meal
        fields = ['name', 'description', 'calories', 'meal_type', 'meal_name_type', 'image_url', 'carbohydrates', 'proteins', 'fats']
        labels = {
            'name': 'Meal Name:',
            'description': 'Description:',
            'calories': 'Calories:',
            'meal_type': 'Meal Type:',
            'meal_name_type': 'Meal Name Type:',
            'image_url': 'Meal Picture:',
            'carbohydrates': 'Carbohydrates:',
            'proteins': 'Proteins:',
            'fats': 'Fats:',
        }
