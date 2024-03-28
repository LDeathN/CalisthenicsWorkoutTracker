from django.core.exceptions import ValidationError
#from .models import Meal


def validate_meal_name(name):
    if not all(ch.isalpha() or ch == " " for ch in name):
        raise ValidationError("Meal name must contain only letters!")

    #for meal in Meal.objects.all():
        #if meal.name == name:
            #raise ValidationError("Meal name is already taken!")
