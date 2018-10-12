from django.urls import path, include ,re_path
from . import views

urlpatterns = [
    
    path('todos/', views.todos, name='todos' ),
    #path(r'todos/(\d+)/completed/', views.completed_todos, name='completed_todos'),

    re_path(r'^todos/(\d+)/completed/$', views.completed_todos),
]    



