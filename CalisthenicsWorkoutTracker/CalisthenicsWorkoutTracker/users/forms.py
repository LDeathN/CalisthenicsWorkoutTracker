from django.contrib.auth import forms as auth_forms, get_user_model
from django import forms
from CalisthenicsWorkoutTracker.users.models import WorkoutTrackerProfiles

UserModel = get_user_model()


class WorkoutTrackerUserCreationForm(auth_forms.UserCreationForm):
    user = None

    class Meta(auth_forms.UserCreationForm.Meta):
        model = UserModel
        fields = ('email',)


class ProfileEditForm(forms.ModelForm):

    class Meta:
        model = WorkoutTrackerProfiles
        fields = ['username', 'first_name', 'last_name', 'date_of_birth', 'profile_picture']
        labels = {
            'username': 'Username:',
            'first_name': 'First Name:',
            'last_name': 'Last Name:',
            'date_of_birth': 'Date of Birth:',
            'profile_picture': 'Profile Picture:',
        }




