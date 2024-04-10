from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from datetime import datetime, timedelta
from CalisthenicsWorkoutTracker.workouts.models import Workout
from CalisthenicsWorkoutTracker.programs.models import Program


class WorkoutDetailsViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = get_user_model()
        cls.user = user.objects.create_user(email="test_address@gmail.com", password='test1password@')

    def setUp(self):
        # Create a test program
        self.client.login(email="test_address@gmail.com", password='test1password@')
        start_date = datetime.now()  # Use the current date and time as the start date
        end_date = start_date + timedelta(days=7)  # Set the end date 7 days after the start date
        self.program = Program.objects.create(
            name='Test Program',
            description='This is a test program',
            start_date=start_date,
            end_date=end_date,
            user_id=self.user.id)

        # Create a test workout associated with the test program
        self.workout = Workout.objects.create(
            name='Test Workout',
            description='This is a test workout',
            difficulty='Medium',
            duration=30,
            image_url='http://example.com/workout.jpg',
            program=self.program,
            user=self.user)

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get(reverse('details_workout', kwargs={'pk': self.workout.pk, 'program_id': self.program.pk}))
        self.assertEqual(response.status_code, 200)  # 200 is the status code for successful HTTP request

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('details_workout', kwargs={'pk': self.workout.pk, 'program_id': self.program.pk}))
        self.assertTemplateUsed(response, 'workouts/workout_details.html')

    def test_context_contains_program(self):
        response = self.client.get(reverse('details_workout', kwargs={'pk': self.workout.pk, 'program_id': self.program.pk}))
        self.assertEqual(response.context['program'], self.program)

    def test_context_contains_workout(self):
        response = self.client.get(reverse('details_workout', kwargs={'pk': self.workout.pk, 'program_id': self.program.pk}))
        self.assertEqual(response.context['workout'], self.workout)
