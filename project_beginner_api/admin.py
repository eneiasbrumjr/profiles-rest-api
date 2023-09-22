from django.contrib import admin
#from django.contrib.auth.admin import UserAdmin
from project_beginner_api import models

# Register your models here.
admin.site.register(models.UserProfile)
