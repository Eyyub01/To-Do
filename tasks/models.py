from django.db import models
from django.utils import timezone

class Task(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField(null=True, blank=True)
    deadline = models.DateTimeField(timezone.now, null=True, blank=True)
    is_completed = models.BooleanField(default=False)
    email_reminder = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name