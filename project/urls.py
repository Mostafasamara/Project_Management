from django.conf.urls import url
from django.urls import path
from .views import (
    ProjectListApiView,
    ProjectDetailApiView
)


urlpatterns = [

    # path('',views.ProjectList),
    path('api', ProjectListApiView.as_view()),
    path('api/<int:project_id>/', ProjectDetailApiView.as_view()),

]
