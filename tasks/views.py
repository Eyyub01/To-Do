from django.shortcuts import render
from .models import *

def task_list_view(request):
    task = Task.objects.all
    context = {
        'tasks': task
    }
    return render(request, 'home.html', context)
