from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.views import generic as views
from CalisthenicsWorkoutTracker.meal_plans.models import MealPlan
from CalisthenicsWorkoutTracker.meals.models import Meal
from CalisthenicsWorkoutTracker.programs.models import Program
from django.contrib.auth import mixins as auth_mixins
from CalisthenicsWorkoutTracker.meals.forms import MealEditForm


class MealCreateView(auth_mixins.LoginRequiredMixin, views.CreateView):
    queryset = Meal.objects.all()
    template_name = 'meals/meal_create.html'
    fields = ['name', 'description', 'calories', 'meal_type', 'meal_name_type']

    def get_success_url(self):
        return reverse_lazy('info_meals', kwargs={'program_id': self.kwargs['program_id'], 'meal_plan_id': self.kwargs['meal_plan_id']})

    def form_valid(self, form):
        meal = form.save(commit=False)
        meal.user = self.request.user
        meal.meal_plan = get_object_or_404(MealPlan, id=self.kwargs['meal_plan_id'])
        meal.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        meal_plan = get_object_or_404(MealPlan, id=self.kwargs['meal_plan_id'])
        program = get_object_or_404(Program, id=self.kwargs['program_id'])
        context['program'] = program
        context['meal_plan'] = meal_plan
        return context


class MealDetailsView(auth_mixins.LoginRequiredMixin, views.DetailView):
    queryset = Meal.objects.all()
    template_name = 'meals/meal_details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        meal_plan = get_object_or_404(MealPlan, id=self.kwargs['meal_plan_id'])
        program = get_object_or_404(Program, id=self.kwargs['program_id'])
        context['program'] = program
        context['meal_plan'] = meal_plan
        return context


class MealEditView(auth_mixins.LoginRequiredMixin, views.UpdateView):
    queryset = Meal.objects.all()
    template_name = 'meals/meal_edit.html'
    form_class = MealEditForm

    def get_success_url(self):
        return reverse_lazy('details_meal', kwargs={'pk': self.object.pk, 'program_id': self.kwargs['program_id'], 'meal_plan_id': self.kwargs['meal_plan_id']})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        meal_plan = get_object_or_404(MealPlan, id=self.kwargs['meal_plan_id'])
        program = get_object_or_404(Program, id=self.kwargs['program_id'])
        context['program'] = program
        context['meal_plan'] = meal_plan
        return context


class MealDeleteView(auth_mixins.LoginRequiredMixin, views.DeleteView):
    queryset = Meal.objects.all()
    template_name = 'meals/meal_delete.html'

    def get_success_url(self):
        return reverse_lazy('info_meals', kwargs={'program_id': self.kwargs['program_id'], 'meal_plan_id': self.kwargs['meal_plan_id']})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        meal_plan = get_object_or_404(MealPlan, id=self.kwargs['meal_plan_id'])
        program = get_object_or_404(Program, id=self.kwargs['program_id'])
        context['form'] = MealEditForm(instance=self.object)
        context['program'] = program
        context['meal_plan'] = meal_plan
        return context

    def get_object(self, queryset=None):
        return Meal.objects.get(pk=self.kwargs['pk'])

    def delete(self, request, *args, **kwargs):
        meal = self.get_object()
        meal.delete()
        return redirect(self.get_success_url())


class MealInfoView(auth_mixins.LoginRequiredMixin, views.TemplateView):
    queryset = Meal.objects.all()
    template_name = 'meals/meal_view_details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        meal_plan = get_object_or_404(MealPlan, id=self.kwargs['meal_plan_id'])
        program = get_object_or_404(Program, id=self.kwargs['program_id'])
        context['meals'] = meal_plan.meals_set.all()
        context['program'] = program
        context['meal_plan'] = meal_plan
        return context
