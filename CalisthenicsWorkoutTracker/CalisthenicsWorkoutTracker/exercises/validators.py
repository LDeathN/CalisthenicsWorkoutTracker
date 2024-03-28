from django.core.exceptions import ValidationError
#from CalisthenicsWorkoutTracker.exercises.models import Exercise


def validate_exercise_name(name):
    if not all(ch.isalpha() or ch == " " for ch in name):
        raise ValidationError("Exercise name must contain only letters!")

    #for exercise in Exercise.objects.all():
        #if exercise.name == name:
            #raise ValidationError("Exercise name is already in use!")


def validate_repetitions(repetitions):
    if repetitions <= 0:
        raise ValidationError("Repetitions must be greater than 0!")
