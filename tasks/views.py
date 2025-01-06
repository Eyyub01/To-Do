from django.shortcuts import render
from django.http import JsonResponse
from .models import *
from django.shortcuts import get_object_or_404

def task_list_view(request):
    task = Task.objects.all
    context = {
        'tasks': task
    }
    return render(request, 'home.html', context)


def add_task(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        deadline = request.POST.get('deadline')
        if not deadline:
            deadline = None  # Set deadline to None if it is not provided
        task = Task.objects.create(name=name, deadline=deadline)
        return JsonResponse({'name': task.name, 'deadline': task.deadline})
    return JsonResponse({'error': 'Invalid request'}, status=400)


def delete_task(request):
    if request.method == 'POST':
        task_id = request.POST.get('task_id')
        Task.objects.filter(id=task_id).delete()
        return JsonResponse({'success': True})
    return JsonResponse({'error': 'Invalid request'}, status=400)
    

def update_task_status(request):
    if request.method == 'POST':
        task_id = request.POST.get('task_id')
        task = get_object_or_404(Task, id=task_id)
        task.is_completed = not task.is_completed  # Toggle the task's completion status
        task.save()
        return JsonResponse({'success': True})
    return JsonResponse({'error': 'Invalid request'}, status=400)




