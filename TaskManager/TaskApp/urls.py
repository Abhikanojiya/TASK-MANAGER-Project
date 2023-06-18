from django.urls import path
from . import views

urlpatterns = [
    path('',views.openLoginForm),
    path('dashboard',views.openDashboard),
    path('user-form',views.openUserForm),
    path('save-user',views.saveUser),
    path('login',views.login),
    path('logout',views.logout),
    path('task-form',views.openTaskForm),
    path('save-task',views.saveTask),
    path('tasks-list',views.getAllTasks),
    path('mark-completed/<int:id>',views.markTaskAsCompleted)
]