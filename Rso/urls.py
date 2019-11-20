from django.urls import path
from .views import (
  RsoListView,
  # RsoDetailView,
  # RsoCreateView
)
from . import views   # '.' = current directory

urlpatterns = [
  path('', 
    RsoListView.as_view(), name='rso-home'),
  # path('event/<int:pk>/',
  #   RsoDetailView.as_view(), name='rso-detail'),
  # path('create/',
  #   RsoCreateView, name='rso-create'),

  

]

