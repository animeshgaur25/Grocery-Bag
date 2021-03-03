from django.contrib import admin

# Register your models here.
from django.contrib import admin
from myapp.models import UserProfileInfo, User

admin.site.register(UserProfileInfo)
