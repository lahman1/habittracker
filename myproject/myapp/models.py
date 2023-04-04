from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Habit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

class HabitEntry(models.Model):
    habit = models.ForeignKey(Habit, on_delete=models.CASCADE)
    completed = models.BooleanField()

class PrebuiltHabit(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name