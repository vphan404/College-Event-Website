from django.urls import path
from .views import (
  UserSignUpView,
  AdminSignUpView,
  SuperAdminSignUpView
)
from . import views   # '.' = current directory

urlpatterns = [
  path('', 
    UserSignUpView.as_view(), name='user-registration'),

  path('admin/',
    AdminSignUpView.as_view(), name='admin-registration'),

  path('event/<int:pk>/',
    SuperAdminSignUpView.as_view(), name='super-admin-registration'),
]

