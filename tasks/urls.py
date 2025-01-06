from django.urls import path
from .views import *


urlpatterns = [
    path('', task_list_view, name='task_list_view'),
    path('add/', add_task, name='add_task'),
    path('delete/', delete_task, name='delete_task'),
    path('update_status/', update_task_status, name='update_task_status'),
]
