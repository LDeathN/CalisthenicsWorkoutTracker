from django.urls import path
from CalisthenicsWorkoutTracker.exercises.views import ExerciseCreateView, ExerciseDetailsView, ExerciseEditView, ExerciseDeleteView, ExerciseInfoView

urlpatterns = [
    path('create/', ExerciseCreateView.as_view(), name='create_exercise'),
    path('details/<int:pk>/', ExerciseDetailsView.as_view(), name='details_exercise'),
    path('edit/<int:pk>/', ExerciseEditView.as_view(), name='edit_exercise'),
    path('delete/<int:pk>/', ExerciseDeleteView.as_view(), name='delete_exercise'),
    path('info/', ExerciseInfoView.as_view(), name='info_exercise'),
]
