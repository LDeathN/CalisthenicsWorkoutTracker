from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.utils import timezone
from CalisthenicsWorkoutTracker.programs.models import Program


class ProgramCreateViewTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = get_user_model()
        cls.user = user.objects.create_user(email="test_address@gmail.com", password='test1password@')

    def test_redirect_if_not_logged_in(self):
        response = self.client.get(reverse('create_program'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/profiles/signin/?next=%2Fprograms%2Fcreate%2F')

    def test_new_program_is_created(self):
        self.client.login(email='test_address@gmail.com', password='test1password@')
        start_date = timezone.now().date()
        end_date = start_date + timezone.timedelta(days=7)
        response = self.client.post(reverse('create_program'), {
            'name': 'Test Program',
            'description': 'This is a test program',
            'start_date': start_date,
            'end_date': end_date,
            'image_url': 'http://example.com/image.jpg'
        })
        self.assertEqual(response.status_code, 302)  # Check if redirected after successful form submission
        self.assertEqual(Program.objects.count(), 1)  # Check if a new program is created
        new_program = Program.objects.first()
        self.assertEqual(new_program.name, 'Test Program')  # Check if program name matches

