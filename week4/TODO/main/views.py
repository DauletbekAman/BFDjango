from django.shortcuts import render
from datetime import datetime, timedelta
from .models import Task


# Create your views here.
def todos(request):
    
    tasks = Task.objects.all() 
    
    context = {
    'task': tasks
    }	
    return render(request, 'main/todo_list.html' ,context)




def completed_todos(request, index):
	
    tasks = Task.objects.all()
    context = {
    'task': tasks
    }
    return render(request, "main/completed_todo_list.html",context)