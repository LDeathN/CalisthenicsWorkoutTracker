from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.views import generic as views
from CalisthenicsWorkoutTracker.workouts.forms import WorkoutEditForm
from django.contrib.auth import mixins as auth_mixins
from CalisthenicsWorkoutTracker.programs.models import Program
from CalisthenicsWorkoutTracker.workouts.models import Workout


class WorkoutCreateView(auth_mixins.LoginRequiredMixin, views.CreateView):
    queryset = Workout.objects.all()
    template_name = 'workouts/workout_create.html'
    fields = ['name', 'description', 'difficulty', 'duration', 'image_url']

    def get_success_url(self):
        return reverse_lazy('info_workout', kwargs={'program_id': self.kwargs['program_id']})

    def form_valid(self, form):
        workout = form.save(commit=False)
        workout.user = self.request.user
        workout.program = get_object_or_404(Program, id=self.kwargs['program_id'])
        workout.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        program = get_object_or_404(Program, id=self.kwargs['program_id'])
        context['program'] = program
        return context


class WorkoutDetailsView(auth_mixins.LoginRequiredMixin, views.DetailView):
    queryset = Workout.objects.all()
    template_name = 'workouts/workout_details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        program = get_object_or_404(Program, id=self.kwargs['program_id'])
        context['program'] = program
        return context


class WorkoutEditView(auth_mixins.LoginRequiredMixin, views.UpdateView):
    queryset = Workout.objects.all()
    template_name = 'workouts/workout_edit.html'
    form_class = WorkoutEditForm

    def get_success_url(self):
        return reverse_lazy('details_workout', kwargs={'pk': self.object.pk, 'program_id': self.kwargs['program_id']})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        program = get_object_or_404(Program, id=self.kwargs['program_id'])
        context['program'] = program
        return context


class WorkoutDeleteView(auth_mixins.LoginRequiredMixin, views.DeleteView):
    queryset = Workout.objects.all()
    template_name = 'workouts/workout_delete.html'

    def get_success_url(self):
        return reverse_lazy('info_workout', kwargs={'program_id': self.kwargs['program_id']})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        program = get_object_or_404(Program, id=self.kwargs['program_id'])
        context['form'] = WorkoutEditForm(instance=self.object)
        context['program'] = program
        return context

    def get_object(self, queryset=None):
        return Workout.objects.get(pk=self.kwargs['pk'])

    def delete(self, request, *args, **kwargs):
        workout = self.get_object()
        workout.delete()
        return redirect(self.get_success_url())


class WorkoutInfoView(auth_mixins.LoginRequiredMixin, views.TemplateView):
    queryset = Workout.objects.all()
    template_name = 'workouts/workout_view_details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        program = get_object_or_404(Program, id=self.kwargs['program_id'])
        context['workouts'] = program.workouts_set.all()
        context['program'] = program
        return context

