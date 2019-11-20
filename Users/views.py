from django.shortcuts import render, redirect
from django.contrib.auth.forms import (
  UserCreationForm
)
from django.views.generic import (
  CreateView
)
from django.contrib import messages
# from django.contrib.auth.forms import User 
from .forms import (
  UserRegistrationForm,
  AdminSignUpForm,
  SuperAdminSignUpForm
)
from .models import (
  User
)

# Create your views here.
# def register(request):
#   if request.method == "POST":
#     form = UserRegistrationForm(request.POST) 
#     if form.is_valid():
#       form.save()
#       username = form.cleaned_data.get('username') 
#       messages.success(request, f'Your account has been created! Please log in')
#       return redirect('login')
#     else:
#       form = UserRegistrationForm() 
#     context = {
#       'form': form,
#     }
#     return render(request, 'Users/register.html', context)

class UserSignUpView(CreateView):
  model = User 
  form_class = UserSignUpForm
  template_name = 'users/signup_form.html'
  
  def get_context_data(self, **kwargs):
    kwargs['user_type'] = 'user'
    return super().get_context_data(**kwargs) 

  def form_valid(self, form):
    user = form.save()
    login(self.request, user) 
    return redirect('events:events-home')

class AdminSignUpView(CreateView):
  model = User 
  form_class = AdminSignUpForm 
  template_name = 'users/signup_form.html'

  def get_context_data(self, **kwargs):
    kwargs['user_type'] = 'admin'
    return super().get_context_data(**kwargs) 

  def form_valid(self, form):
    user = form.save()
    login(self.request, user) 
    return redirect('events:events-home')