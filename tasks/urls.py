from django.urls import path
from .views import *


urlpatterns = [
    path('', task_list_view, name='task_list_view')
]