from django.conf.urls import url
from django.urls import path
from .views import (
    ProjectListApiView,
    ProjectDetailApiView,
    TaskListApiView,
    TaskDetailApiView
)


urlpatterns = [

    # path('',views.ProjectList),
    path('api', ProjectListApiView.as_view()),
    path('api/<int:project_id>/', ProjectDetailApiView.as_view()),
    #url of task
    path('task', TaskListApiView.as_view()),
    path('task/<int:task_id>/', TaskDetailApiView.as_view()),

]
