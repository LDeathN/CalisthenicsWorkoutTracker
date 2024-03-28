from CalisthenicsWorkoutTracker.workouts.models import Workout
from django import forms


class WorkoutEditForm(forms.ModelForm):

    class Meta:
        model = Workout
        fields = ['name', 'description', 'difficulty', 'duration', 'image_url']
        labels = {
            'name': 'Workout Name:',
            'description': 'Description:',
            'difficulty': 'Difficulty:',
            'duration': 'Duration:',
            'image_url': 'Workout Picture:',
        }
