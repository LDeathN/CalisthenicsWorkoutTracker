from django.urls import path, include
from CalisthenicsWorkoutTracker.meal_plans.views import MealPlanCreateView, MealPlanDeleteView, MealPlanEditView, MealPlanDetailsView, MealPlanInfoView

urlpatterns = [
    path('create/', MealPlanCreateView.as_view(), name='create_meal_plan'),
    path('details/<int:pk>/', MealPlanDetailsView.as_view(), name='details_meal_plan'),
    path('edit/<int:pk>/', MealPlanEditView.as_view(), name='edit_meal_plan'),
    path('delete/<int:pk>/', MealPlanDeleteView.as_view(), name='delete_meal_plan'),
    path('info/', MealPlanInfoView.as_view(), name='info_meal_plan'),
    path('<int:meal_plan_id>/meal/', include('CalisthenicsWorkoutTracker.meals.urls')),
]
