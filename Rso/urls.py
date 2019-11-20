from django.urls import path

from . import views   # '.' = current directory

urlpatterns = [
  path('', 
    views.rso, name='rso-home'),
]