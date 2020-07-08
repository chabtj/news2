from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm,CustomUserChangeForm
from .models import CustomUserModel
# Register your models here.
class CustomUserAdmin(UserAdmin):
	form=CustomUserChangeForm
	add_form=CustomUserCreationForm
	model=CustomUserModel

admin.site.register(CustomUserModel,CustomUserAdmin)