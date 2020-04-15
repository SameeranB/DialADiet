from django.db import models

# Create your models here.
from users.models import User


class Diets(models.Model):
    diet_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, models.CASCADE, related_name='diets')
    diet_number = models.IntegerField()
    notes = models.TextField(blank=True)
    preset = models.BooleanField(default=False)
    name = models.CharField(max_length=100, blank=True)


class DietData(models.Model):
    related_diet = models.ForeignKey(Diets, on_delete=models.CASCADE, related_name='data')
    time = models.TimeField()
    type = models.CharField(max_length=50, choices=(
        ('Early Morning', 'Early Morning'),
        ('Mid Meal', 'Mid Meal'),
        ('Lunch', 'Lunch'),
        ('Evening Meal 1', 'Evening Meal 1'),
        ('Evening Meal 2', 'Evening Meal 2'),
        ('Dinner', 'Dinner'),
        ('Late Night', 'Late Night')
    ))
    body = models.TextField()
