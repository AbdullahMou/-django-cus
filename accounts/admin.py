

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
# ​from django.contrib.auth import get_user_model
from .forms import *

class CustomUserAdmin(UserAdmin):
    add_form=CustomUserCreationForm
    form=CustomUserChangeForm
    model=CustomUser
    list_display=['first_name','last_name','email']



# Register your models here.
admin.site.register(CustomUser,CustomUserAdmin)