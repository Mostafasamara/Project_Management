from django.contrib import admin
from django.urls import path , include
from project import urls as project_urls
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from project.views import ProjectListApiView, TaskListApiView


router = DefaultRouter()
router.register(r'project', ProjectListApiView, basename='project')
router.register(r'task', TaskListApiView, basename='task')

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include(user.urls)),
    path('user/', include('user.urls')),
    path('project/', include(project_urls)),
    # path('user/', include('user.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
