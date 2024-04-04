from django.contrib import admin
from CalisthenicsWorkoutTracker.programs.models import Program


@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'start_date', 'end_date')
    list_filter = ('start_date', 'end_date', 'user')
    ordering = ('-start_date',)

