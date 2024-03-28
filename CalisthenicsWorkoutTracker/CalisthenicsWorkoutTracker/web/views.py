from django.shortcuts import render
from CalisthenicsWorkoutTracker.programs.models import Program


def index(request):
    context = {
    }

    return render(request, 'web/index.html', context)


def dashboard(request):

    programs = Program.objects.all()

    context = {
        'programs': programs,
    }

    return render(request, 'web/dashboard.html', context)
