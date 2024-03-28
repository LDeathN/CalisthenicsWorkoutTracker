from django.core.exceptions import ValidationError
#from CalisthenicsWorkoutTracker.meal_plans.models import MealPlan


def validate_meal_plan_name(name):
    if not all(ch.isalpha() or ch == " " for ch in name):
        raise ValidationError("Meal plan name must contain only letters!")

    #for meal_plan in MealPlan.objects.all():
        #if meal_plan.name == name:
            #raise ValidationError("Meal plan name is already taken!")
