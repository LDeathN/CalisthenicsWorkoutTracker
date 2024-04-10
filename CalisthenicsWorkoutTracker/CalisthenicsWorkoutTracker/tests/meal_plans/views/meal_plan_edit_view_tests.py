from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from datetime import datetime, timedelta
from CalisthenicsWorkoutTracker.meal_plans.models import MealPlan
from CalisthenicsWorkoutTracker.programs.models import Program
from CalisthenicsWorkoutTracker.meal_plans.views import MealPlanEditView


class MealPlanEditViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = get_user_model()
        cls.user = user.objects.create_user(email="test_address@gmail.com", password='test1password@')

    def setUp(self):
        # Log in the user
        self.client.login(email="test_address@gmail.com", password='test1password@')
        # Create a test program
        start_date = datetime.now()
        end_date = start_date + timedelta(days=7)
        self.program = Program.objects.create(
            name='Test Program',
            description='This is a test program',
            start_date=start_date,
            end_date=end_date,
            user_id=self.user.id)

        # Create a test meal plan associated with the test program
        self.meal_plan = MealPlan.objects.create(
            name='Test Meal Plan',
            description='This is a test meal plan',
            program=self.program,
            goal_calories=2000,
            user_id=self.user.id
        )

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get(reverse('edit_meal_plan', kwargs={'pk': self.meal_plan.pk, 'program_id': self.program.pk}))
        self.assertEqual(response.status_code, 200)  # 200 is the status code for successful HTTP request

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('edit_meal_plan', kwargs={'pk': self.meal_plan.pk, 'program_id': self.program.pk}))
        self.assertTemplateUsed(response, 'meal_plans/meal_plan_edit.html')

    def test_context_contains_program(self):
        response = self.client.get(reverse('edit_meal_plan', kwargs={'pk': self.meal_plan.pk, 'program_id': self.program.pk}))
        self.assertEqual(response.context['program'], self.program)

    def test_context_contains_meal_plan(self):
        response = self.client.get(reverse('edit_meal_plan', kwargs={'pk': self.meal_plan.pk, 'program_id': self.program.pk}))
        self.assertEqual(response.context['mealplan'], self.meal_plan)

    def test_get_success_url(self):
        view = MealPlanEditView()
        view.object = self.meal_plan
        view.kwargs = {'program_id': self.program.pk}
        self.assertEqual(view.get_success_url(), reverse('details_meal_plan', kwargs={'pk': self.meal_plan.pk, 'program_id': self.program.pk}))

