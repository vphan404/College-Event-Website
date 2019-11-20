from django.urls import path
from .views import (
  ChooseSignUpView,
  UserSignUpView,
  AdminSignUpView,
  SuperAdminSignUpView
)
from . import views   # '.' = current directory

urlpatterns = [ 
  path('', 
    ChooseSignUpView.as_view(), name='register'),

  path('user/', 
    UserSignUpView.as_view(), name='user-registration'),

  path('admin/',
    AdminSignUpView.as_view(), name='admin-registration'),

  path('superadmin',
    SuperAdminSignUpView.as_view(), name='super-admin-registration'),
]

