from django.urls import path, include
from CalisthenicsWorkoutTracker.programs.views import ProgramCreateView, ProgramDetailsView, ProgramEditView, ProgramDeleteView, ProgramInfoView

urlpatterns = [
    path('create/', ProgramCreateView.as_view(), name='create_program'),
    path('details/<int:pk>/', ProgramDetailsView.as_view(), name='details_program'),
    path('edit/<int:pk>/', ProgramEditView.as_view(), name='edit_program'),
    path('delete/<int:pk>/', ProgramDeleteView.as_view(), name='delete_program'),
    path('info/<int:pk>/', ProgramInfoView.as_view(), name='info_program'),
    path('<int:program_id>/workout/', include('CalisthenicsWorkoutTracker.workouts.urls')),
    path('<int:program_id>/meal_plan/', include('CalisthenicsWorkoutTracker.meal_plans.urls')),
]
