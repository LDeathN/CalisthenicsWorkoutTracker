# Generated by Django 5.0.2 on 2024-03-11 17:28

import CalisthenicsWorkoutTracker.exercises.validators
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, validators=[django.core.validators.MinLengthValidator(3), CalisthenicsWorkoutTracker.exercises.validators.validate_exercise_name], verbose_name='Exercise Name')),
                ('description', models.TextField(blank=True, max_length=200, null=True, verbose_name='Description')),
                ('difficulty', models.IntegerField(choices=[(1, 'Easy'), (2, 'Moderate'), (3, 'Intermediate'), (4, 'Challenging'), (5, 'Advanced')], help_text='1-5 (Easy to Advanced)', verbose_name='Difficulty')),
                ('repetitions', models.PositiveIntegerField(default=6, validators=[django.core.validators.MaxValueValidator(30), CalisthenicsWorkoutTracker.exercises.validators.validate_repetitions], verbose_name='Repetitions')),
            ],
        ),
    ]