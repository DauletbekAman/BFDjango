from django.urls import path, include
from . import views

urlpatterns = [
    
    path('todos/', views.todos, name='todos' ),
    path('todos/1/completed/', views.completed_todos, name='completed_todos'),
]