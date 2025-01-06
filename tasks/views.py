from datetime import timedelta

from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from django.core.mail import send_mail
from django.http import JsonResponse
from django.utils import timezone

from .models import Task

def task_list_view(request):
    tasks = Task.objects.all()
    context = {
        'tasks': tasks
    }
    return render(request, 'home.html', context)

def add_task(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        deadline = request.POST.get('deadline')
        email_reminder = request.POST.get('email_reminder') == 'on'
        if not deadline:
            deadline = None
        task = Task.objects.create(name=name, deadline=deadline, email_reminder=email_reminder)
        
        if email_reminder:
            send_immediate_reminder_email(task)
            if deadline:
                send_reminder_email(task)
        
        return redirect('task_list_view')
    return JsonResponse({'error': 'Invalid request'}, status=400)

def send_immediate_reminder_email(task):
    send_mail(
        'New Task Created',
        f'You have created a new task: {task.name}. Deadline: {task.deadline}',
        'abbaszadeeyyub@gmail.com',
        ['abbaszade.mesume@icloud.com'],
    )

def send_reminder_email(task):
    reminder_time = task.deadline - timedelta(hours=1)
    print(reminder_time)
    current_time = timezone.now()
    
    if current_time >= reminder_time:
        send_mail(
            'Task Reminder',
            f'Remember to complete the task: {task.name} before the deadline: {task.deadline}',
            'abbaszadeeyyub@gmail.com',
            ['abbaszadeeyyub222@gmail.com'], 
        )

def delete_task(request):
    if request.method == 'POST':
        task_id = request.POST.get('task_id')
        task = get_object_or_404(Task, id=task_id)
        task.delete()
        return JsonResponse({'success': True})
    return JsonResponse({'error': 'Invalid request'}, status=400)

def update_task_status(request):
    if request.method == 'POST':
        task_id = request.POST.get('task_id')
        task = get_object_or_404(Task, id=task_id)
        task.is_completed = not task.is_completed
        task.save()
        return JsonResponse({'success': True})
    return JsonResponse({'error': 'Invalid request'}, status=400)
