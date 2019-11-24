from django import forms 
from django.db import transaction
from django.contrib.auth.forms import UserCreationForm 
from .models import ( 
  User,
  Profile
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

class UserUpdateForm(forms.ModelForm):
  email = forms.EmailField()

  class Meta:
    model = User
    fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
  class Meta:
    model = Profile
    fields = ['image']