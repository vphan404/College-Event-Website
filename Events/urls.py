from django.urls import path
from .views import (
  EventListView,
  EventDetailView,
  EventCreateView
)
from . import views   # '.' = current directory

urlpatterns = [
  path('', 
    # views.home, name='events-home'),
    EventListView.as_view(), name='events-home'),

  # path('test/', 
  #   EventListView.as_view(), name='event-list'),

  path('create/',
    EventCreateView.as_view(), name='event-create'),
  
  path('event/<int:pk>/',
    EventDetailView.as_view(), name='event-detail'),

  path('about/', 
    views.about, name='events-about'),
  
  # path('registered-student-organizations/', 
  #   views.RSO, name='events-RSO')
]

