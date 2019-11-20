from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.views.generic import (
  CreateView,
  TemplateView
)
from django.contrib import messages
from .forms import (
  UserSignUpForm,
  AdminSignUpForm,
  SuperAdminSignUpForm,
  UserUpdateForm,
  ProfileUpdateForm
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


@login_required
def profile(request):
  return render(request, 'Users/profile.html')

def edit_profile(request):
  if request.method == 'POST':
    u_form = UserUpdateForm(request.POST, instance=request.user)
    p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

    if u_form.is_valid() and p_form.is_valid():
      u_form.save()
      p_form.save()

      messages.success(request, f'Your account has been updated!')
      return redirect('profile')
  else:
    u_form = UserUpdateForm(instance=request.user)
    p_form = ProfileUpdateForm(instance=request.user.profile)

  context = {
    'u_form': u_form,
    'p_form': p_form
  }

  return render(request, 'Users/edit_profile.html', context)


class ChooseSignUpView(TemplateView):
  template_name = 'users/choose_signup.html'


class UserSignUpView(CreateView):
  model = User 
  form_class = UserSignUpForm
  template_name = 'users/signup_form_user.html'
  
  def get_context_data(self, **kwargs):
    kwargs['user_type'] = 'user'
    context = super().get_context_data(**kwargs) 
    return context

  def form_valid(self, form):
    user = form.save()
    login(self.request, user) 
    # messages.success(request, f'Your account has been created! Please log in.')
    return redirect('events-home')


class AdminSignUpView(CreateView):
  model = User 
  form_class = AdminSignUpForm 
  template_name = 'users/signup_form_admin.html'

  def get_context_data(self, **kwargs):
    kwargs['user_type'] = 'admin'
    return super().get_context_data(**kwargs) 

  def form_valid(self, form):
    user = form.save()
    login(self.request, user) 
    return redirect('events-home')


class SuperAdminSignUpView(CreateView):
  model = User 
  form_class = SuperAdminSignUpForm 
  template_name = 'users/signup_form_super_admin.html'

  def get_context_data(self, **kwargs):
    kwargs['user_type'] = 'admin'
    return super().get_context_data(**kwargs) 

  def form_valid(self, form):
    user = form.save()
    login(self.request, user) 
    return redirect('events-home')

