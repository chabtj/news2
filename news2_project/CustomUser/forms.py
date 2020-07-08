from django import forms 
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from .models import CustomUserModel
class CustomUserCreationForm(UserCreationForm):
	class Meta (UserCreationForm.Meta):
		fields=UserCreationForm.Meta.fields+('age',)
		model=CustomUserModel
class CustomUserChangeForm(UserChangeForm):
	class Meta(UserChangeForm.Meta):
		fields=UserChangeForm.Meta.fields
		model=CustomUserModel