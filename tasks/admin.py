from django.contrib import admin
from .models import *

class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_completed', 'created_at', 'updated_at')
    list_filter = ('is_completed', 'created_at', 'updated_at', 'deadline')
    search_fields = ('name', 'description')
    actions = ['mark_as_completed']

    def mark_as_completed(self, request, queryset):
        queryset.update(is_completed=True)
    mark_as_completed.short_description = "Mark selected tasks as completed"

admin.site.register(Task, TaskAdmin)
