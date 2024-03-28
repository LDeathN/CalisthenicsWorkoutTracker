from django.urls import path
from CalisthenicsWorkoutTracker.meals.views import MealCreateView, MealEditView, MealDetailsView, MealDeleteView, MealInfoView

urlpatterns = [
    path('create/', MealCreateView.as_view(), name='create_meal'),
    path('details/<int:pk>/', MealDetailsView.as_view(), name='details_meal'),
    path('edit/<int:pk>/', MealEditView.as_view(), name='edit_meal'),
    path('delete/<int:pk>/', MealDeleteView.as_view(), name='delete_meal'),
    path('info/', MealInfoView.as_view(), name='info_meals'),
]
