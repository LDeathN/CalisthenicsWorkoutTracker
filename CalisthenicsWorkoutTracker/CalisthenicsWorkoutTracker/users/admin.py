from django.contrib import admin
from CalisthenicsWorkoutTracker.users.models import WorkoutTrackerUser


@admin.register(WorkoutTrackerUser)
class WorkoutTrackerUserAdmin(admin.ModelAdmin):
    list_display = ('email',)

