from django.urls import path
from . import views
from .views import CustomLoginView, register
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('home/', views.home, name='home'),
    path('logout/', LogoutView.as_view(template_name='registration/logout.html'), name='myapp_logout'),
    path('add_habit/', views.add_habit, name='add_habit'),
    path('add_habit_entry/<int:habit_id>/', views.add_habit_entry, name='add_habit_entry'),
    path('delete_habit/<int:habit_id>/', views.delete_habit, name='delete_habit'),
    path('edit_habit/<int:habit_id>/', views.edit_habit, name='edit_habit'),
    path('update_habit_order', views.update_habit_order, name='update_habit_order'),
    path('prebuilt_habits/', views.prebuilt_habits, name='prebuilt_habits'),
]