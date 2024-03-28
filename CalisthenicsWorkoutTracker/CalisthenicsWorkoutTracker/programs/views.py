from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.views import generic as views
from CalisthenicsWorkoutTracker.programs.models import Program
from django.contrib.auth import mixins as auth_mixins
from CalisthenicsWorkoutTracker.programs.forms import ProgramEditForm


class ProgramCreateView(auth_mixins.LoginRequiredMixin, views.CreateView):
    queryset = Program.objects.all()
    fields = ['name', 'description', 'start_date', 'end_date', 'image_url']
    template_name = 'programs/program_create.html'
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        program = form.save(commit=False)
        program.user = self.request.user
        program.save()
        return super().form_valid(form)


class ProgramDetailsView(auth_mixins.LoginRequiredMixin, views.DetailView):
    queryset = Program.objects.all()
    template_name = 'programs/program_details.html'


class ProgramEditView(auth_mixins.LoginRequiredMixin, views.UpdateView):
    queryset = Program.objects.all()
    template_name = 'programs/program_edit.html'
    form_class = ProgramEditForm

    def get_success_url(self):
        return reverse_lazy('details_program', kwargs={'pk': self.object.pk})


class ProgramDeleteView(auth_mixins.LoginRequiredMixin, views.DeleteView):
    queryset = Program.objects.all()
    template_name = 'programs/program_delete.html'
    success_url = reverse_lazy('dashboard')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ProgramEditForm(instance=self.object)
        return context

    def get_object(self, queryset=None):
        return Program.objects.get(pk=self.kwargs['pk'])

    def delete(self, request, *args, **kwargs):
        program = self.get_object()
        program.delete()
        return redirect(self.get_success_url())


class ProgramInfoView(auth_mixins.LoginRequiredMixin, views.DetailView):
    queryset = Program.objects.all()
    template_name = 'programs/program_view_details.html'

