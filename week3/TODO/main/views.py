from django.shortcuts import render
from datetime import datetime, timedelta

# Create your views here.

def todos(request):
	today = datetime.today()
	todo_list = [
	{

		'title': "Task {}".format(i),
        'created': today.strftime("%d/%m/%y"),
        'due_on': (today + timedelta(days=2)).strftime("%d/%m/%y"),
        'owner': "admin",
        'mark': True
     }
     
     for i in range(1,5)

	]

	return render(request, 'main/todo_list.html' , {'todo_list': todo_list})




def completed_todos(request):
	today = datetime.today()

	task = {


		'title': "Task 0",
        'created': today.strftime("%d/%m/%y"),
        'due_on': (today + timedelta(days=2)).strftime("%d/%m/%y"),
        'owner': "admin",
        'mark': False
       }

     


	return render(request, "main/completed_todo_list.html", {'task': task})