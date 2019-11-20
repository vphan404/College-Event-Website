from django.urls import path
from .views import (
  User
)
from . import views   # '.' = current directory

urlpatterns = [
  path('', 
    
    # views.home, name='events-home'),
    EventListView.as_view(), name='events-home'),

  # path('test/', 
  #   EventListView.as_view(), name='event-list'),

  path('create/',
    # EventCreateView.as_view(), name='event-create'),
    EventCreateView, name='event-create'),

  path('event/<int:pk>/',
    EventDetailView.as_view(), name='event-detail'),

  
  # path('registered-student-organizations/', 
  #   views.RSO, name='events-RSO')
]

