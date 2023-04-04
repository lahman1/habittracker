from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Habit, HabitEntry, PrebuiltHabit
from .forms import HabitForm, HabitEntryForm, PrebuiltHabitForm
import json


# Create your views here.

def index(request):
    return render(request, 'index.html')

@login_required
def home(request):
    habits = Habit.objects.filter(user=request.user).order_by('order')
    return render(request, 'home.html', {'habits': habits})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'

@login_required
def add_habit(request):
    if request.method == 'POST':
        form = HabitForm(request.POST)
        if form.is_valid():
            habit = form.save(commit=False)
            habit.user = request.user
            habit.save()
            return redirect('home')
    else:
        form = HabitForm
    return render(request, 'myapp/add_habit.html', {'form': form})

@login_required
def add_habit_entry(request, habit_id):
    habit = Habit.objects.get(id=habit_id)
    if request.method == 'POST':
        form = HabitEntryForm(request.POST)
        if form.is_valid():
            habit_entry = form.save(commit=False)
            habit_entry.habit = habit
            habit_entry.save()
            return redirect('home')
    else:
        form = HabitEntryForm()
    return render(request, 'myapp/add_habit_entry.html', {'form': form, 'habit': habit})

@login_required
def delete_habit(request, habit_id):
    habit = get_object_or_404(Habit, pk=habit_id, user=request.user)
    habit.delete()
    return redirect('home')

@login_required
def edit_habit(request, habit_id):
    habit = get_object_or_404(Habit, pk=habit_id, user=request.user)
    if request.method == 'POST':
        form = HabitForm(request.POST, instance=habit)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = HabitForm(instance=habit)
    return render(request, 'myapp/edit_habit.html', {'form': form})

@csrf_exempt
@login_required
def update_habit_order(request):
    if request.method == 'POST':
        habit_order = json.loads(request.POST['order'])
        for index, habit_id in enumerate(habit_order):
            habit = Habit.objects.get(id=habit_id, user=request.user)
            habit.order = index
            habit.save()
        return JsonResponse({"status": "success"})
    else:
        return JsonResponse({"status": "error"})
    
@login_required
def prebuilt_habits(request):
    prebuilt_habits = PrebuiltHabit.objects.all()
    if request.method == 'POST':
        form = PrebuiltHabitForm(request.POST)
        if form.is_valid():
            selected_habits = form.cleaned_data['habits']
            for habit in selected_habits:
                Habit.objects.create(user=request.user, name=habit.name, description=habit.description)
            return redirect('home')
    else:
        form = PrebuiltHabitForm()
    
    return render(request, 'myapp/prebuilt_habits.html', {'form':form})

