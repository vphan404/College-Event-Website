from django import forms 
from django.db import transaction
from django.contrib.auth.forms import UserCreationForm 
from .models import ( 
  User
)

class UserSignUpForm(UserCreationForm):
  email = forms.EmailField() 

  class Meta(UserCreationForm.Meta):
    model = User 
    fields = [
      'username',
      'email',
      'password1',
      'password2'
    ]


class AdminSignUpForm(UserCreationForm):
  email = forms.EmailField() 
  class Meta(UserCreationForm.Meta):
    model = User
  
  @transaction.atomic
  def save(self):
    user = super().save(commit=False)
    user.is_admin = True 
    user.save()
    return user


class SuperAdminSignUpForm(UserCreationForm):
  email = forms.EmailField() 
  class Meta(UserCreationForm.Meta):
    model = User
  
  @transaction.atomic
  def save(self):
    user = super().save(commit=False)
    user.is_admin = True 
    user.save()
    return user