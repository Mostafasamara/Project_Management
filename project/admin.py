from django.contrib import admin

# Register your models here.
from .models import Project,Task

@admin.register(Project)

class ProjectAdmin(admin.ModelAdmin):
    list_display = ['project_name','user','created_at']


@admin.register(Task)

class TaskAdmin(admin.ModelAdmin):
    list_display = ['project','task_name','created_by','created_at','start_date','end_date']
