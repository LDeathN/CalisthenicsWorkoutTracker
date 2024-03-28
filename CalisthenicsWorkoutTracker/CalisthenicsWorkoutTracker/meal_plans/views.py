from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.views import generic as views
from django.contrib.auth import mixins as auth_mixins
from CalisthenicsWorkoutTracker.meal_plans.models import MealPlan
from CalisthenicsWorkoutTracker.programs.models import Program
from CalisthenicsWorkoutTracker.meal_plans.forms import MealPlanEditForm


class MealPlanCreateView(auth_mixins.LoginRequiredMixin, views.CreateView):
    queryset = MealPlan.objects.all()
    template_name = 'meal_plans/meal_plan_create.html'
    fields = ['name', 'description', 'meal_plan_type', 'goal_calories']

    def get_success_url(self):
        return reverse_lazy('info_meal_plan', kwargs={'program_id': self.kwargs['program_id']})

    def form_valid(self, form):
        meal_plan = form.save(commit=False)
        meal_plan.user = self.request.user
        meal_plan.program = get_object_or_404(Program, id=self.kwargs['program_id'])
        meal_plan.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        program = get_object_or_404(Program, id=self.kwargs['program_id'])
        context['program'] = program
        return context


class MealPlanDetailsView(auth_mixins.LoginRequiredMixin, views.DetailView):
    queryset = MealPlan.objects.all()
    template_name = 'meal_plans/meal_plan_details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        program = get_object_or_404(Program, id=self.kwargs['program_id'])
        context['program'] = program
        return context


class MealPlanEditView(auth_mixins.LoginRequiredMixin, views.UpdateView):
    queryset = MealPlan.objects.all()
    template_name = 'meal_plans/meal_plan_edit.html'
    form_class = MealPlanEditForm

    def get_success_url(self):
        return reverse_lazy('details_meal_plan', kwargs={'pk': self.object.pk, 'program_id': self.kwargs['program_id']})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        program = get_object_or_404(Program, id=self.kwargs['program_id'])
        context['program'] = program
        return context


class MealPlanDeleteView(auth_mixins.LoginRequiredMixin, views.DeleteView):
    queryset = MealPlan.objects.all()
    template_name = 'meal_plans/meal_plan_delete.html'

    def get_success_url(self):
        return reverse_lazy('info_meal_plan', kwargs={'program_id': self.kwargs['program_id']})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        program = get_object_or_404(Program, id=self.kwargs['program_id'])
        context['form'] = MealPlanEditForm(instance=self.object)
        context['program'] = program
        return context

    def get_object(self, queryset=None):
        return MealPlan.objects.get(pk=self.kwargs['pk'])

    def delete(self, request, *args, **kwargs):
        meal_plan = self.get_object()
        meal_plan.delete()
        return redirect(self.get_success_url())


class MealPlanInfoView(auth_mixins.LoginRequiredMixin, views.TemplateView):
    queryset = MealPlan.objects.all()
    template_name = 'meal_plans/meal_plan_view_details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        program = get_object_or_404(Program, id=self.kwargs['program_id'])
        context['meal_plans'] = program.meal_plans_set.all()
        context['program'] = program
        return context
