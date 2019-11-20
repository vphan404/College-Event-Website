from django.urls import path
from . import views   # '.' = current directory

urlpatterns = [
  path('',
    views.RSO, name='RSO-RSO'),
]