from django.contrib import admin
from CalisthenicsWorkoutTracker.workouts.models import Workout


@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'difficulty', 'duration')
    list_filter = ('program', 'difficulty')
    search_fields = ('name', 'program__name')

