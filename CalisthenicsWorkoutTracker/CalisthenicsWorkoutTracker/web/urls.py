from django.urls import path
from CalisthenicsWorkoutTracker.web.views import index, dashboard

urlpatterns = [
    path('', index, name='index'),
    path('dashboard/', dashboard, name='dashboard'),
]

