from django.core.exceptions import ValidationError
#from CalisthenicsWorkoutTracker.workouts.models import Workout


def validate_workout_name(name):
    if not all(ch.isalpha() or ch == " " for ch in name):
        raise ValidationError("Workout name must contain only letters!")

    #for workout in Workout.objects.all():
        #if workout.name == name:
            #raise ValidationError("Workout name is already in use!")
