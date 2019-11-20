from django import forms 
# from django.contrib.auth.models import User 
from django.db import transaction
from django.contrib.auth.forms import UserCreationForm 
from .models import ( 
  User
)

class UserRegistrationForm(UserCreationForm):
  email = forms.EmailField() 

  class Meta:
    model = User 
    fields = [
      'username',
      'email',
      'password1',
      'password2'
    ]

class AdminSignUpForm(UserCreationForm):
  class Meta(UserCreationForm.Meta):
    model = User
  
  @transaction.atomic
  def save(self):
    user = super().save(commit=False)
    user.is_admin = True 
    user.save()
    return user

class SuperAdminSignUpForm(UserCreationForm):
  class Meta(UserCreationForm.Meta):
    model = User
  
  @transaction.atomic
  def save(self):
    user = super().save(commit=False)
    user.is_admin = True 
    user.save()
    return user