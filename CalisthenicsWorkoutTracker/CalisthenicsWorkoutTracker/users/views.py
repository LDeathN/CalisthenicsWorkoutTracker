from django.shortcuts import redirect
from django.views import generic as views
from CalisthenicsWorkoutTracker.users.models import WorkoutTrackerProfiles
from django.urls import reverse_lazy
from django.contrib.auth import views as auth_views
from django.contrib.auth import login, logout
from django.contrib.auth import mixins as auth_mixins
from CalisthenicsWorkoutTracker.users.forms import WorkoutTrackerUserCreationForm, ProfileEditForm
from CalisthenicsWorkoutTracker.workouts.models import Workout
from CalisthenicsWorkoutTracker.programs.models import Program
from CalisthenicsWorkoutTracker.meal_plans.models import MealPlan

class SignInUserView(auth_views.LoginView):
    template_name = 'web/login.html'
    redirect_authenticated_user = True


class SignUpUserView(views.CreateView):
    template_name = 'web/register.html'
    form_class = WorkoutTrackerUserCreationForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, form.instance)
        return result


def logout_user(request):
    logout(request)
    return redirect('index')


class ProfileDetailsView(auth_mixins.LoginRequiredMixin, views.DetailView):
    queryset = WorkoutTrackerProfiles.objects.prefetch_related("user").all()
    template_name = 'profiles/profile_details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['programs'] = Program.objects.filter(user=user)
        context['workouts'] = Workout.objects.filter(user=user)
        context['meal_plans'] = MealPlan.objects.filter(user=user)
        return context


class ProfileEditView(auth_mixins.LoginRequiredMixin, views.UpdateView):
    queryset = WorkoutTrackerProfiles.objects.all()
    template_name = 'profiles/profile_edit.html'
    form_class = ProfileEditForm

    def get_success_url(self):
        return reverse_lazy("details_user", kwargs={"pk": self.object.pk})


class ProfileDeleteView(auth_mixins.LoginRequiredMixin, views.DeleteView):
    queryset = WorkoutTrackerProfiles.objects.all()
    template_name = 'profiles/profile_delete.html'
    success_url = reverse_lazy('index')

    def get_object(self, queryset=None):
        return self.request.user

    def delete(self, request, *args, **kwargs):
        user = self.get_object()
        user.delete()
        return redirect(self.get_success_url())
