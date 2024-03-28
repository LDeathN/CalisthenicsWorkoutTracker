from django.urls import path, include
from CalisthenicsWorkoutTracker.workouts.views import WorkoutCreateView, WorkoutEditView, WorkoutDeleteView, WorkoutDetailsView, WorkoutInfoView

urlpatterns = [
    path('create/', WorkoutCreateView.as_view(), name='create_workout'),
    path('details/<int:pk>/', WorkoutDetailsView.as_view(), name='details_workout'),
    path('edit/<int:pk>/', WorkoutEditView.as_view(), name='edit_workout'),
    path('delete/<int:pk>/', WorkoutDeleteView.as_view(), name='delete_workout'),
    path('info/', WorkoutInfoView.as_view(), name='info_workout'),
    path('<int:workout_id>/exercise/', include('CalisthenicsWorkoutTracker.exercises.urls'))
]

