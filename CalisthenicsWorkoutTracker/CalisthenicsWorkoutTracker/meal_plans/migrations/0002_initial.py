# Generated by Django 5.0.2 on 2024-03-11 17:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('meal_plans', '0001_initial'),
        ('programs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mealplan',
            name='program',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='meal_plans', to='programs.program', verbose_name='Program'),
        ),
    ]