from django import forms
from .models import Habit, HabitEntry, PrebuiltHabit

class HabitForm(forms.ModelForm):
    class Meta:
        model = Habit
        fields = ["name", "description"]

class HabitEntryForm(forms.ModelForm):
    class Meta:
        model = HabitEntry
        fields = ['habit', 'completed']

class PrebuiltHabitForm(forms.ModelForm):
    habits = forms.ModelMultipleChoiceField(
        queryset=PrebuiltHabit.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    class Meta:
        model = PrebuiltHabit
        fields = ['habits']