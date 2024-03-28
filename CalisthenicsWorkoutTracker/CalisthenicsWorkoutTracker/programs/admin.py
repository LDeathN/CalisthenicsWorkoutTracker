from django.contrib import admin
from CalisthenicsWorkoutTracker.programs.models import Program


@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'start_date', 'end_date')

