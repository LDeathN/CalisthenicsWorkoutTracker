from CalisthenicsWorkoutTracker.programs.models import Program
from django import forms


class ProgramEditForm(forms.ModelForm):

    class Meta:
        model = Program
        fields = ['name', 'description', 'start_date', 'end_date', 'image_url']
        labels = {
            'name': 'Program Name:',
            'description': 'Description:',
            'start_date': 'Start Date:',
            'end_date': 'End Date:',
            'image_url': 'Program Picture:',
        }
