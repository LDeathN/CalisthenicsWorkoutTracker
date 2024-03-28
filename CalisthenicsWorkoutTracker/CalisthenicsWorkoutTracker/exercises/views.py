from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.views import generic as views
from CalisthenicsWorkoutTracker.exercises.models import Exercise
from CalisthenicsWorkoutTracker.workouts.models import Workout
from CalisthenicsWorkoutTracker.programs.models import Program
from django.contrib.auth import mixins as auth_mixins
from CalisthenicsWorkoutTracker.exercises.forms import ExerciseEditForm


class ExerciseCreateView(auth_mixins.LoginRequiredMixin, views.CreateView):
    queryset = Exercise.objects.all()
    template_name = 'exercises/exercise_create.html'
    fields = ['name', 'description', 'difficulty', 'repetitions']

    def get_success_url(self):
        return reverse_lazy('info_exercise', kwargs={'program_id': self.kwargs['program_id'], 'workout_id': self.kwargs['workout_id']})

    def form_valid(self, form):
        exercise = form.save(commit=False)
        exercise.user = self.request.user
        exercise.workout = get_object_or_404(Workout, id=self.kwargs['workout_id'])
        exercise.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        workout = get_object_or_404(Workout, id=self.kwargs['workout_id'])
        program = get_object_or_404(Program, id=self.kwargs['program_id'])
        context['program'] = program
        context['workout'] = workout
        return context


class ExerciseDetailsView(auth_mixins.LoginRequiredMixin, views.DetailView):
    queryset = Exercise.objects.all()
    template_name = 'exercises/exercise_details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        workout = get_object_or_404(Workout, id=self.kwargs['workout_id'])
        program = get_object_or_404(Program, id=self.kwargs['program_id'])
        context['program'] = program
        context['workout'] = workout
        return context


class ExerciseEditView(auth_mixins.LoginRequiredMixin, views.UpdateView):
    queryset = Exercise.objects.all()
    template_name = 'exercises/exercise_edit.html'
    form_class = ExerciseEditForm

    def get_success_url(self):
        return reverse_lazy('details_exercise', kwargs={'pk': self.object.pk, 'program_id': self.kwargs['program_id'], 'workout_id': self.kwargs['workout_id']})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        workout = get_object_or_404(Workout, id=self.kwargs['workout_id'])
        program = get_object_or_404(Program, id=self.kwargs['program_id'])
        context['program'] = program
        context['workout'] = workout
        return context


class ExerciseDeleteView(auth_mixins.LoginRequiredMixin, views.DeleteView):
    queryset = Exercise.objects.all()
    template_name = 'exercises/exercise_delete.html'

    def get_success_url(self):
        return reverse_lazy('info_exercise', kwargs={'program_id': self.kwargs['program_id'], 'workout_id': self.kwargs['workout_id']})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        workout = get_object_or_404(Workout, id=self.kwargs['workout_id'])
        program = get_object_or_404(Program, id=self.kwargs['program_id'])
        context['form'] = ExerciseEditForm(instance=self.object)
        context['program'] = program
        context['workout'] = workout
        return context

    def get_object(self, queryset=None):
        return Exercise.objects.get(pk=self.kwargs['pk'])

    def delete(self, request, *args, **kwargs):
        exercise = self.get_object()
        exercise.delete()
        return redirect(self.get_success_url())


class ExerciseInfoView(auth_mixins.LoginRequiredMixin, views.TemplateView):
    queryset = Exercise.objects.all()
    template_name = 'exercises/exercise_view_details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        workout = get_object_or_404(Workout, id=self.kwargs['workout_id'])
        program = get_object_or_404(Program, id=self.kwargs['program_id'])
        context['exercises'] = workout.exercises_set.all()
        context['program'] = program
        context['workout'] = workout
        return context
