from django.contrib import admin
from CalisthenicsWorkoutTracker.exercises.models import Exercise


@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'difficulty', 'repetitions',)

