from django.db import models
from django.contrib.auth.models import User
from project.models import Project
# Create your models here.


class Userprofile(models.Model):
    user = models.OneToOneField(User,related_name="userprofile",on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254,blank=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d/',blank=True)
    # projects = models.ForeignKey(Project,related_name='projects',on_delete=models.CASCADE,blank=True)
    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)
