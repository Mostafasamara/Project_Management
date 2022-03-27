from django.contrib import admin
from django.urls import path , include
from project import urls as project_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('rest-auth/', include('rest_auth.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('project/', include(project_urls)),

]
