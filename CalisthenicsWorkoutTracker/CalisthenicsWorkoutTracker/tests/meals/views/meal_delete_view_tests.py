from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from datetime import datetime, timedelta
from CalisthenicsWorkoutTracker.meal_plans.models import MealPlan
from CalisthenicsWorkoutTracker.programs.models import Program
from CalisthenicsWorkoutTracker.meals.models import Meal
from CalisthenicsWorkoutTracker.meals.views import MealDeleteView


class MealDeleteViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = get_user_model()
        cls.user = user.objects.create_user(email="test_address@gmail.com", password='test1password@')

    def setUp(self):
        # Create a test program
        self.client.login(email="test_address@gmail.com", password='test1password@')
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

        # Create a test meal associated with the test meal plan
        self.meal = Meal.objects.create(
            name='Test Meal',
            description='This is a test meal',
            meal_plan=self.meal_plan,
            calories=500,
            user_id=self.user.id)

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get(reverse('delete_meal', kwargs={'pk': self.meal.pk, 'program_id': self.program.pk, 'meal_plan_id': self.meal_plan.pk}))
        self.assertEqual(response.status_code, 200)  # 200 is the status code for successful HTTP request

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('delete_meal', kwargs={'pk': self.meal.pk, 'program_id': self.program.pk, 'meal_plan_id': self.meal_plan.pk}))
        self.assertTemplateUsed(response, 'meals/meal_delete.html')

    def test_context_contains_meal(self):
        response = self.client.get(reverse('delete_meal', kwargs={'pk': self.meal.pk, 'program_id': self.program.pk, 'meal_plan_id': self.meal_plan.pk}))
        self.assertEqual(response.context['meal'], self.meal)

    def test_context_contains_program(self):
        response = self.client.get(reverse('delete_meal', kwargs={'pk': self.meal.pk, 'program_id': self.program.pk, 'meal_plan_id': self.meal_plan.pk}))
        self.assertEqual(response.context['program'], self.program)

    def test_context_contains_meal_plan(self):
        response = self.client.get(reverse('delete_meal', kwargs={'pk': self.meal.pk, 'program_id': self.program.pk, 'meal_plan_id': self.meal_plan.pk}))
        self.assertEqual(response.context['meal_plan'], self.meal_plan)

    def test_get_success_url(self):
        view = MealDeleteView()
        view.kwargs = {'program_id': self.program.pk, 'meal_plan_id': self.meal_plan.pk}
        self.assertEqual(view.get_success_url(), reverse('info_meals', kwargs={'program_id': self.program.pk, 'meal_plan_id': self.meal_plan.pk}))
