from CalisthenicsWorkoutTracker.exercises.models import Exercise
from django import forms


class ExerciseEditForm(forms.ModelForm):

    class Meta:
        model = Exercise
        fields = ['name', 'description', 'difficulty', 'repetitions']
        labels = {
            'name': 'Exercise Name:',
            'description': 'Description:',
            'difficulty': 'Difficulty:',
            'repetitions': 'Repetitions:',
        }
