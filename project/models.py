# django imports
from django.contrib.auth.models import User
from django.db import models
from team.models import Team
# project scheama

class Project(models.Model):
    project_name = models.CharField(max_length=100)
    user = models.ForeignKey(User,related_name='projects',on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    team = models.ForeignKey(Team, related_name='projects', on_delete=models.CASCADE)
    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.project_name


class Task(models.Model):
    project = models.ForeignKey(Project,related_name='tasks',on_delete=models.CASCADE)
    task_name = models.CharField(max_length=100)
    user = models.ForeignKey(User,related_name='tasks',on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    start_date = models.DateTimeField(auto_now=False)
    end_date = models.DateTimeField(auto_now=False)
    desc = models.TextField(blank=True)

    def __str__(self):
        return self.task_name
