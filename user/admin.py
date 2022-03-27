from django.contrib import admin

# Register your models here.
from .models import Userprofile
@admin.register(Userprofile)
class ProfileAdmin(admin.ModelAdmin):

    list_display = ['user','first_name','last_name','email']